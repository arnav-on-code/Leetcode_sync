from config.settings import Config

from leetcode.auth import LeetCodeAuth
from leetcode.client import LeetCodeClient
from leetcode.api import LeetCodeAPI
from leetcode.downloader import SubmissionDownloader

from sync.detector import SubmissionDetector

from github_sync.manager import GitManager
from github_sync.messages import generate_commit_message
from github_sync.statistics import StatisticsManager
from github_sync.readme import ReadmeGenerator


class SyncManager:
    """
    Coordinates the complete LeetCode synchronization workflow.
    """

    def __init__(self):
        session = LeetCodeAuth().get_session()

        self.api = LeetCodeAPI(
            LeetCodeClient(session)
        )

        self.detector = SubmissionDetector()

        self.downloader = SubmissionDownloader()

        self.statistics = StatisticsManager()

        self.readme = ReadmeGenerator()

        self.git = GitManager(Config.BASE_DIR)

    def run(self):
        """
        Run one synchronization cycle.
        """

        # Fetch profile once
        profile = self.api.get_profile()

        # Fetch recent accepted submissions
        submissions = self.api.get_recent_submissions()

        # Detect new submissions
        new_submissions = self.detector.find_new(submissions)

        if not new_submissions:
            print("No new submissions found.")
            return

        print(f"Found {len(new_submissions)} new submission(s).\n")

        for submission in new_submissions:
            try:
                # Fetch complete submission details
                detail = self.api.get_submission_detail(
                    submission.id
                )

                # Download solution
                self.downloader.download(detail)

                # Update statistics
                stats = self.statistics.update(
                    profile,
                    detail,
                )

                # Generate README
                readme_path = self.readme.generate(stats)

                print(f"✓ README updated: {readme_path}")

                # Generate commit message
                commit_message = generate_commit_message(detail)

                # Git add + commit + push
                self.git.sync(commit_message)

                # Update state only after successful Git sync
                self.detector.update(submission)

                print(f"✓ Synced: {submission.title}")

            except Exception as e:
                print(f"✗ Failed: {submission.title}")
                print(e)

        print("\nSynchronization complete.")
from config.settings import Config
from github_sync.manager import GitManager
from github_sync.messages import generate_commit_message
from leetcode.api import LeetCodeAPI
from leetcode.auth import LeetCodeAuth
from leetcode.client import LeetCodeClient
from leetcode.downloader import SubmissionDownloader
from sync.detector import SubmissionDetector


class SyncManager:
    """
    Coordinates the complete LeetCode synchronization workflow.
    """

    def __init__(self):
        session = LeetCodeAuth().get_session()

        self.api = LeetCodeAPI(LeetCodeClient(session))

        self.detector = SubmissionDetector()

        self.downloader = SubmissionDownloader()

        self.git = GitManager(Config.BASE_DIR)

    def run(self):
        """
        Run one synchronization cycle.
        """

        # Fetch recent accepted submissions
        submissions = self.api.get_recent_submissions()

        # Detect which ones haven't been synced yet
        new_submissions = self.detector.find_new(submissions)

        if not new_submissions:
            print("No new submissions found.")
            return

        print(f"Found {len(new_submissions)} new submission(s).\n")

        for submission in new_submissions:
            try:
                # Fetch complete submission details
                detail = self.api.get_submission_detail(submission.id)

                # Download solution and metadata
                self.downloader.download(detail)

                self.git.add()

                self.git.commit(generate_commit_message(detail))

                self.git.push()

                self.detector.update(submission)

                print(f"✓ Synced: {submission.title}")

            except Exception as e:
                print(f"✗ Failed: {submission.title}")
                print(e)

        print("\nSynchronization complete.")

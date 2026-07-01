from config.settings import Config

from leetcode.auth import LeetCodeAuth
from leetcode.client import LeetCodeClient
from leetcode.api import LeetCodeAPI
from leetcode.downloader import SubmissionDownloader

from sync.detector import SubmissionDetector

from github_sync.manager import GitManager
from github_sync.messages import generate_commit_message


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

        self.git = GitManager(Config.BASE_DIR)

    def run(self):
        """
        Run one synchronization cycle.
        """

        submissions = self.api.get_recent_submissions()

        new_submissions = self.detector.find_new(submissions)

        if not new_submissions:
            print("No new submissions found.")
            return

        latest = new_submissions[0]

        detail = self.api.get_submission_detail(latest.id)

        self.downloader.download(detail)

        self.git.add()

        self.git.commit(
            generate_commit_message(detail)
        )

        self.git.push()

        self.detector.update(latest)

        print(f"Successfully synced: {latest.title}")
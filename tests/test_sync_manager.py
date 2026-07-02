from unittest.mock import MagicMock, patch

from leetcode.models import Submission, SubmissionDetail
from sync.manager import SyncManager


@patch("sync.manager.GitManager")
@patch("sync.manager.SubmissionDownloader")
@patch("sync.manager.SubmissionDetector")
@patch("sync.manager.LeetCodeAPI")
@patch("sync.manager.LeetCodeClient")
@patch("sync.manager.LeetCodeAuth")
def test_sync_manager_run(
    mock_auth,
    mock_client,
    mock_api,
    mock_detector,
    mock_downloader,
    mock_git,
):

    manager = SyncManager()

    submission = Submission(
        id="1",
        title="Two Sum",
        slug="two-sum",
        timestamp=1780000000,
    )

    detail = SubmissionDetail(
        submission_id="1",
        question_id="1",
        title_slug="two-sum",
        language="python3",
        language_verbose="Python3",
        runtime=45,
        runtime_display="45 ms",
        memory=17000000,
        memory_display="17 MB",
        status_code=10,
        code="print('hello')",
        timestamp=1780000000,
    )

    manager.api.get_recent_submissions = MagicMock(return_value=[submission])

    manager.detector.find_new = MagicMock(return_value=[submission])

    manager.api.get_submission_detail = MagicMock(return_value=detail)

    manager.downloader.download = MagicMock()

    manager.git.sync = MagicMock()

    manager.detector.update = MagicMock()

    manager.run()

    manager.api.get_recent_submissions.assert_called_once()

    manager.detector.find_new.assert_called_once()

    manager.api.get_submission_detail.assert_called_once()

    manager.downloader.download.assert_called_once()

    manager.git.sync.assert_called_once()

    manager.detector.update.assert_called_once()


@patch("sync.manager.GitManager")
@patch("sync.manager.SubmissionDownloader")
@patch("sync.manager.SubmissionDetector")
@patch("sync.manager.LeetCodeAPI")
@patch("sync.manager.LeetCodeClient")
@patch("sync.manager.LeetCodeAuth")
def test_sync_manager_no_new_submissions(
    mock_auth,
    mock_client,
    mock_api,
    mock_detector,
    mock_downloader,
    mock_git,
):

    manager = SyncManager()

    manager.api.get_recent_submissions = MagicMock(return_value=[])

    manager.detector.find_new = MagicMock(return_value=[])

    manager.run()

    manager.detector.find_new.assert_called_once()

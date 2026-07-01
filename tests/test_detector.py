from unittest.mock import patch

from leetcode.models import Submission
from sync.detector import SubmissionDetector


def test_find_new_first_run():

    detector = SubmissionDetector()

    detector.state = {"last_submission_id": None}

    submissions = [
        Submission(
            id="3",
            title="C",
            slug="c",
            timestamp=3,
        ),
        Submission(
            id="2",
            title="B",
            slug="b",
            timestamp=2,
        ),
        Submission(
            id="1",
            title="A",
            slug="a",
            timestamp=1,
        ),
    ]

    new = detector.find_new(submissions)

    assert len(new) == 3


@patch("sync.detector.StateManager.save")
def test_update_state(mock_save, sample_submission):

    detector = SubmissionDetector()

    detector.update(sample_submission)

    mock_save.assert_called_once_with(sample_submission.id)


def test_find_new_after_update(sample_submission):

    detector = SubmissionDetector()

    detector.state = {"last_submission_id": sample_submission.id}

    submissions = [
        sample_submission,
    ]

    new = detector.find_new(submissions)

    assert new == []

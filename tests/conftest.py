import pytest

from leetcode.models import Submission, SubmissionDetail


@pytest.fixture
def sample_submission():

    return Submission(
        id="2051842379",
        title="Find Median from Data Stream",
        slug="find-median-from-data-stream",
        timestamp=1782879665,
    )


@pytest.fixture
def sample_submission_detail(sample_detail):
    """
    Alias for backward compatibility.
    """
    return sample_detail


@pytest.fixture
def sample_detail():
    return SubmissionDetail(
        submission_id="2051842379",
        question_id="295",
        title_slug="find-median-from-data-stream",
        language="python3",
        language_verbose="Python3",
        runtime=177,
        runtime_display="177 ms",
        memory=41264000,
        memory_display="41.3 MB",
        status_code=10,
        code="print('hello')",
        timestamp=1782879665,
    )


@pytest.fixture
def temp_solution_dir(tmp_path):
    """
    Temporary directory for downloader tests.
    """

    return tmp_path / "solutions"

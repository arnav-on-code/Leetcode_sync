import json

from leetcode.downloader import SubmissionDownloader


def test_create_problem_directory(
    tmp_path,
    sample_submission_detail,
):

    downloader = SubmissionDownloader()

    downloader.solutions_dir = tmp_path

    folder = downloader.create_problem_directory(
        sample_submission_detail
    )

    assert folder.exists()

    assert folder.is_dir()


def test_save_solution(
    tmp_path,
    sample_submission_detail,
):

    downloader = SubmissionDownloader()

    downloader.solutions_dir = tmp_path

    folder = downloader.create_problem_directory(
        sample_submission_detail
    )

    solution = downloader.save_solution(
        folder,
        sample_submission_detail,
    )

    assert solution.exists()

    assert solution.name == "solution.py"

    assert (
        solution.read_text(encoding="utf-8")
        == sample_submission_detail.code
    )


def test_save_metadata(
    tmp_path,
    sample_submission_detail,
):

    downloader = SubmissionDownloader()

    downloader.solutions_dir = tmp_path

    folder = downloader.create_problem_directory(
        sample_submission_detail
    )

    metadata = downloader.save_metadata(
        folder,
        sample_submission_detail,
    )

    assert metadata.exists()

    data = json.loads(
        metadata.read_text(
            encoding="utf-8"
        )
    )

    assert data["question_id"] == "295"

    assert data["language"] == "python3"

    assert data["status_code"] == 10


def test_download(
    tmp_path,
    sample_submission_detail,
):

    downloader = SubmissionDownloader()

    downloader.solutions_dir = tmp_path

    folder = downloader.download(
        sample_submission_detail
    )

    assert folder.exists()

    assert (
        folder / "solution.py"
    ).exists()

    assert (
        folder / "metadata.json"
    ).exists()
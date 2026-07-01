from pathlib import Path

from config.settings import Config


class SubmissionDownloader:
    """
    Handles downloading and storing LeetCode submissions locally.
    """

    def __init__(self):
        self.solutions_dir = Config.STORAGE_DIR / "solutions"

        # Create storage/solutions if it doesn't exist
        self.solutions_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    @staticmethod
    def _format_folder_name(question_id: str, slug: str) -> str:
        """
        Convert:
            295
            find-median-from-data-stream

        Into:
            0295_Find_Median_from_Data_Stream
        """

        problem_number = str(question_id).zfill(4)

        title = "_".join(
            word.capitalize()
            for word in slug.split("-")
        )

        return f"{problem_number}_{title}"

    def create_problem_directory(self, detail) -> Path:
        """
        Create the directory for a problem if it doesn't already exist.
        """

        folder_name = self._format_folder_name(
            detail.question_id,
            detail.title_slug,
        )

        problem_dir = self.solutions_dir / folder_name

        problem_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        return problem_dir
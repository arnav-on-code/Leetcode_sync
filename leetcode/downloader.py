import json
from pathlib import Path

from config.settings import Config


class SubmissionDownloader:
    

    LANGUAGE_FILES = {
        "python3": "solution.py",
        "python": "solution.py",
        "java": "Solution.java",
        "cpp": "solution.cpp",
        "c": "solution.c",
        "javascript": "solution.js",
        "typescript": "solution.ts",
        "go": "solution.go",
        "rust": "solution.rs",
        "kotlin": "Solution.kt",
        "swift": "solution.swift",
        "csharp": "Solution.cs",
    }

    def __init__(self):
        self.solutions_dir = Config.STORAGE_DIR / "solutions"
        self.solutions_dir.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_solution_filename(cls, language: str) -> str:
        return cls.LANGUAGE_FILES.get(
            language.lower(),
            "solution.txt",
        )

    @staticmethod
    def _format_folder_name(question_id: str, slug: str) -> str:
        problem_number = str(question_id).zfill(4)

        title = "_".join(
            word.capitalize()
            for word in slug.split("-")
        )

        return f"{problem_number}_{title}"

    def create_problem_directory(self, detail) -> Path:
        folder_name = self._format_folder_name(
            detail.question_id,
            detail.title_slug,
        )

        problem_dir = self.solutions_dir / folder_name
        problem_dir.mkdir(parents=True, exist_ok=True)

        return problem_dir

    def save_solution(self, problem_dir: Path, detail) -> Path:
        
        filename = self.get_solution_filename(detail.language)

        solution_file = problem_dir / filename

        solution_file.write_text(
            detail.code,
            encoding="utf-8",
        )

        return solution_file


    def save_metadata(self, problem_dir: Path, detail) -> Path:
        

        metadata = {
            "submission_id": detail.submission_id,
            "question_id": detail.question_id,
            "title_slug": detail.title_slug,
            "language": detail.language,
            "language_verbose": detail.language_verbose,
            "runtime": detail.runtime_display,
            "memory": detail.memory_display,
            "status_code": detail.status_code,
            "timestamp": detail.timestamp,
        }

        metadata_file = problem_dir / "metadata.json"

        metadata_file.write_text(
            json.dumps(metadata, indent=4),
            encoding="utf-8",
        )

        return metadata_file

    def download(self, detail) -> Path:
      

        problem_dir = self.create_problem_directory(detail)

        self.save_solution(problem_dir, detail)

        self.save_metadata(problem_dir, detail)

        return problem_dir
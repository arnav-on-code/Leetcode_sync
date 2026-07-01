from pathlib import Path
import shutil
import subprocess


class GitManager:
    """
    Handles Git operations for the repository.
    """

    def __init__(self, repository: Path):
        if shutil.which("git") is None:
            raise RuntimeError(
                "Git is not installed or not available in PATH."
            )

        self.repository = Path(repository).resolve()

    def run(self, *args: str) -> str:
        try:
            result = subprocess.run(
                ["git", *args],
                cwd=self.repository,
                capture_output=True,
                text=True,
                check=True,
            )

            return result.stdout.strip()

        except subprocess.CalledProcessError as e:
            raise RuntimeError(e.stderr.strip()) from e

    def status(self) -> str:
        return self.run("status", "--short")

    def add(self) -> None:
        self.run("add", ".")

    def commit(self, message: str) -> None:
        self.run("commit", "-m", message)

    def push(self) -> None:
        self.run("push")

    def pull(self) -> None:
        self.run("pull")
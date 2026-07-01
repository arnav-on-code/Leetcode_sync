from pathlib import Path
import subprocess


class GitManager:
    """
    Handles Git operations for the repository.
    """

    def __init__(self, repository: Path):
        self.repository = Path(repository)

    def run(self, *args):
        """
        Execute a git command inside the repository.
        """

        result = subprocess.run(
            ["git", *args],
            cwd=self.repository,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())

        return result.stdout.strip()

    def status(self):
        return self.run("status", "--short")

    def add(self):
        self.run("add", ".")

    def commit(self, message: str):
        self.run("commit", "-m", message)

    def push(self):
        self.run("push")

    def pull(self):
        self.run("pull")
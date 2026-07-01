from pathlib import Path
from unittest.mock import MagicMock, patch

from github_sync.manager import GitManager


def test_status():

    manager = GitManager(Path("."))

    with patch("subprocess.run") as mock_run:

        mock = MagicMock()

        mock.returncode = 0

        mock.stdout = "M main.py"

        mock_run.return_value = mock

        assert manager.status() == "M main.py"


def test_add():

    manager = GitManager(Path("."))

    with patch("subprocess.run") as mock_run:

        mock = MagicMock()

        mock.returncode = 0

        mock.stdout = ""

        mock_run.return_value = mock

        manager.add()

        assert mock_run.called


def test_commit():

    manager = GitManager(Path("."))

    with patch("subprocess.run") as mock_run:

        mock = MagicMock()

        mock.returncode = 0

        mock.stdout = ""

        mock_run.return_value = mock

        manager.commit("test commit")

        assert mock_run.called


def test_push():

    manager = GitManager(Path("."))

    with patch("subprocess.run") as mock_run:

        mock = MagicMock()

        mock.returncode = 0

        mock.stdout = ""

        mock_run.return_value = mock

        manager.push()

        assert mock_run.called

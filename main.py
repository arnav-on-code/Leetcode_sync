from rich.console import Console
from rich.panel import Panel

from leetcode.auth import LeetCodeAuth
from leetcode.api import LeetCodeAPI

console = Console()


def banner():
    console.print(
        Panel.fit(
            "[bold cyan]LeetCode Sync[/bold cyan]\n"
            "Automatic LeetCode → GitHub Synchronization",
            title="v0.2.0",
        )
    )


def main():
    banner()

    auth = LeetCodeAuth()
    api = LeetCodeAPI(auth.get_session())

    if api.validate_session():
        console.print("[green]✓ Session is valid[/green]")
    else:
        console.print("[red]✗ Invalid session[/red]")


if __name__ == "__main__":
    main()
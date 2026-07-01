from rich.console import Console
from rich.panel import Panel

console = Console()
def banner():
    console.print(
        Panel.fit(
            "[bold cyan]LeetCode Sync[/bold cyan]\n"
            "Automatic LeetCode → GitHub Synchronization",
            title="v0.1.0",
        )
    )
def main():
    banner()

    console.print("[green]Project initialized successfully.[/green]")
    console.print("Next milestone: Authenticate with LeetCode.")


if __name__ == "__main__":
    main()
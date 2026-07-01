from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from sync.detector import SubmissionDetector


from leetcode.auth import LeetCodeAuth
from leetcode.client import LeetCodeClient
from leetcode.api import LeetCodeAPI
from config.settings import Config


console = Console()


def banner():
    console.print(
        Panel.fit(
            "[bold cyan]LeetCode Sync[/bold cyan]\n"
            "Automatic LeetCode → GitHub Synchronization",
            title="v0.4.0",
        )
    )


def display_statistics(stats):
    """Display solved problem statistics."""

    table = Table(title="LeetCode Statistics")

    table.add_column("Difficulty", style="cyan")
    table.add_column("Solved", justify="right", style="green")

    for item in stats:
        table.add_row(
            item["difficulty"],
            str(item["count"])
        )

    console.print(table)


def display_recent_submissions(submissions):
    """Display recent accepted submissions."""

    table = Table(title="Recent Accepted Submissions")

    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Date")

    for submission in submissions:
        table.add_row(
            submission.id,
            submission.title,
            submission.date.strftime("%Y-%m-%d %H:%M"),
        )

    console.print(table)


def main():
    Config.validate()
    Config.initialize()

    banner()

    session = LeetCodeAuth().get_session()
    api = LeetCodeAPI(
        LeetCodeClient(session)
    )

    # Profile
    profile = api.get_profile()

    console.print(
        f"[bold green]Logged in as:[/bold green] {profile['username']}\n"
    )

    display_statistics(
        profile["submitStatsGlobal"]["acSubmissionNum"]
    )

    console.print()

    # Recent submissions
    submissions = api.get_recent_submissions()


    detector = SubmissionDetector()

    new_submissions = detector.find_new(submissions)

    if new_submissions:
        console.print(
            f"\n[bold green]Found {len(new_submissions)} new submission(s).[/bold green]\n"
        )
    else:
        console.print(
            "\n[bold blue]No new submissions found.[/bold blue]\n"
        )

    for submission in new_submissions:
        console.print(f"• {submission.title}")

    display_recent_submissions(submissions)

    if new_submissions:
        detector.update(new_submissions[0])


if __name__ == "__main__":
    main()
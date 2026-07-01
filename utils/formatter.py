from typing import Iterable

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from leetcode.constants import STATUS_MAP

console = Console()


def display_banner() -> None:
    """
    Display the application banner.
    """

    console.print(
        Panel.fit(
            "[bold cyan]LeetCode Sync[/bold cyan]\n"
            "Automatic LeetCode → GitHub Synchronization",
            title="v0.5.0",
        )
    )


def display_profile(username: str) -> None:
    """
    Display logged-in user.
    """

    console.print(
        f"[bold green]Logged in as:[/bold green] {username}\n"
    )


def display_statistics(stats: Iterable[dict]) -> None:
    """
    Display solved problem statistics.
    """

    table = Table(title="LeetCode Statistics")

    table.add_column("Difficulty", style="cyan")
    table.add_column(
        "Solved",
        justify="right",
        style="green",
    )

    for item in stats:
        table.add_row(
            item["difficulty"],
            str(item["count"]),
        )

    console.print(table)


def display_recent_submissions(submissions) -> None:
    """
    Display recent accepted submissions.
    """

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


def display_submission_detail(detail) -> None:
    """
    Display information about a submission.
    """

    table = Table(title="Latest Submission Details")

    table.add_column("Field", style="cyan")
    table.add_column("Value")

    table.add_row(
        "Question ID",
        str(detail.question_id),
    )

    table.add_row(
        "Slug",
        detail.title_slug,
    )

    table.add_row(
        "Language",
        detail.language_verbose,
    )

    table.add_row(
        "Runtime",
        detail.runtime_display,
    )

    table.add_row(
        "Memory",
        detail.memory_display,
    )

    table.add_row(
        "Status",
        STATUS_MAP.get(
            detail.status_code,
            "Unknown",
        ),
    )

    console.print(table)


def display_new_submissions(new_submissions) -> None:
    """
    Display newly detected submissions.
    """

    if not new_submissions:
        console.print(
            "\n[bold blue]No new submissions found.[/bold blue]\n"
        )
        return

    console.print(
        f"\n[bold green]Found {len(new_submissions)} new submission(s).[/bold green]\n"
    )

    for submission in new_submissions:
        console.print(
            f"• {submission.title}"
        )


def display_download(path) -> None:
    """
    Display downloaded solution path.
    """

    console.print(
        f"\n[bold green]Solution saved:[/bold green]\n{path}"
    )


def display_sync_success(title: str) -> None:
    """
    Display synchronization success.
    """

    console.print(
        f"\n[bold green]Successfully synced:[/bold green] {title}"
    )


def display_error(message: str) -> None:
    """
    Display an error message.
    """

    console.print(
        f"\n[bold red]Error:[/bold red] {message}"
    )
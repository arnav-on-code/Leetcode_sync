from pathlib import Path

from config.settings import Config


class ReadmeGenerator:
    """
    Generates the project's README.md automatically.
    """

    def __init__(self):
        self.readme = Config.BASE_DIR / "README.md"

    @staticmethod
    def progress_bar(current: int, total: int = 300, width: int = 30) -> str:
        """
        Generate a unicode progress bar.
        """
        filled = int((current / total) * width)
        filled = min(filled, width)

        return "█" * filled + "░" * (width - filled)

    def generate(self, stats) -> Path:
        """
        Generate README.md from statistics.
        """

        latest = stats.get("last_problem")

        language_lines = []

        for language, count in sorted(
            stats["languages"].items(),
            key=lambda item: item[1],
            reverse=True,
        ):
            language_lines.append(f"- **{language}** : {count}")

        languages = "\n".join(language_lines)

        recent = ""

        for problem in stats.get(
            "recent_problems",
            [],
        ):
            recent += f'- {problem["id"]} ' f'{problem["title"]}\n'

        if latest:
            latest_problem = f"""
| Field | Value |
|------|------|
| Problem ID | {latest["id"]} |
| Title | {latest["title"]} |
| Language | {latest["language"]} |
| Runtime | {latest["runtime"]} |
| Memory | {latest["memory"]} |
"""
        else:
            latest_problem = "No submissions yet."

        progress = self.progress_bar(stats["total"])

        content = f"""# 🚀 LeetCode Sync

Automatically synchronize accepted LeetCode submissions to GitHub.

---

## 📈 Progress

```text
{progress}

Solved: {stats["total"]} / 300 Problems

📊 Statistics
Difficulty	Solved
🟢 Easy	{stats["easy"]}
🟡 Medium	{stats["medium"]}
🔴 Hard	{stats["hard"]}
Total	{stats["total"]}
🔥 Latest Accepted Problem

{latest_problem}

💻 Languages Used

{languages}

## 📚 Recent Accepted Problems

{recent}

---

✨ Features
Automatic LeetCode synchronization
Automatic Git commits
Automatic GitHub push
Metadata generation
README generation
GitHub Actions support
Unit tests
📂 Repository Structure
storage/
└── solutions/
    ├── 0011_Container_With_Most_Water/
    │   ├── solution.py
    │   └── metadata.json
    └── ....
⚙️ Workflow
LeetCode
    │
    ▼
API
    │
    ▼
Downloader
    │
    ▼
Statistics
    │
    ▼
README Generator
    │
    ▼
Git
    │
    ▼
GitHub
⏰ Last Sync

{stats["last_sync"]}
"""

        self.readme.write_text(
            content,
            encoding="utf-8",
        )

        return self.readme

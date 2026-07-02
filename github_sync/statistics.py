import json
from datetime import datetime

from config.settings import Config


class StatisticsManager:
    """
    Maintains repository statistics used by README generation.
    """

    def __init__(self):
        self.stats_file = Config.STORAGE_DIR / "stats.json"

        if not self.stats_file.exists():
            self._create_default()

    def _create_default(self):
        """
        Create the initial stats file.
        """

        default = {
            "total": 0,
            "easy": 0,
            "medium": 0,
            "hard": 0,
            "languages": {},
            "last_problem": None,
            "last_sync": None,
        }

        self.stats_file.write_text(
            json.dumps(default, indent=4),
            encoding="utf-8",
        )

    def load(self):
        """
        Load current statistics.
        """

        return json.loads(
            self.stats_file.read_text(
                encoding="utf-8",
            )
        )

    def save(self, stats):
        """
        Save statistics.
        """

        self.stats_file.write_text(
            json.dumps(
                stats,
                indent=4,
            ),
            encoding="utf-8",
        )

    def update(self, profile, detail):
        """
        Update statistics using latest profile and submission.
        """

        stats = self.load()

        solved = {
            item["difficulty"]: item["count"]
            for item in profile["submitStatsGlobal"]["acSubmissionNum"]
        }

        stats["total"] = solved.get("All", 0)
        stats["easy"] = solved.get("Easy", 0)
        stats["medium"] = solved.get("Medium", 0)
        stats["hard"] = solved.get("Hard", 0)

        language = detail.language_verbose

        languages = stats.get("languages", {})

        languages[language] = (
            languages.get(language, 0) + 1
        )

        stats["languages"] = languages

        stats["last_problem"] = {
            "id": detail.question_id,
            "title": detail.title_slug.replace("-", " ").title(),
            "language": detail.language_verbose,
            "runtime": detail.runtime_display,
            "memory": detail.memory_display,
        }

        stats["last_sync"] = datetime.now().isoformat()

        self.save(stats)

        return stats
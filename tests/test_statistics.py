
from github_sync.statistics import StatisticsManager


def test_create_default(tmp_path):
    manager = StatisticsManager()

    manager.stats_file = tmp_path / "stats.json"

    manager._create_default()

    assert manager.stats_file.exists()


def test_load_default(tmp_path):
    manager = StatisticsManager()

    manager.stats_file = tmp_path / "stats.json"

    manager._create_default()

    stats = manager.load()

    assert stats["total"] == 0
    assert stats["languages"] == {}
    assert stats["recent_problems"] == []


def test_save(tmp_path):
    manager = StatisticsManager()

    manager.stats_file = tmp_path / "stats.json"

    manager._create_default()

    stats = manager.load()

    stats["total"] = 100

    manager.save(stats)

    loaded = manager.load()

    assert loaded["total"] == 100


def test_update(sample_detail):
    manager = StatisticsManager()

    profile = {
        "submitStatsGlobal": {
            "acSubmissionNum": [
                {"difficulty": "All", "count": 121},
                {"difficulty": "Easy", "count": 63},
                {"difficulty": "Medium", "count": 52},
                {"difficulty": "Hard", "count": 6},
            ]
        }
    }

    stats = manager.update(
        profile,
        sample_detail,
    )

    assert stats["total"] == 121

    assert stats["last_problem"]["id"] == sample_detail.question_id

    assert stats["languages"]["Python3"] >= 1

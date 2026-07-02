from github_sync.readme import ReadmeGenerator


def test_generate(tmp_path):
    generator = ReadmeGenerator()

    generator.readme = tmp_path / "README.md"

    stats = {
        "total": 121,
        "easy": 63,
        "medium": 52,
        "hard": 6,
        "languages": {
            "Python3": 121,
        },
        "last_problem": {
            "id": "295",
            "title": "Find Median From Data Stream",
            "language": "Python3",
            "runtime": "177 ms",
            "memory": "41.3 MB",
        },
        "recent_problems": [
            {
                "id": "295",
                "title": "Find Median From Data Stream",
            }
        ],
        "last_sync": "2026-07-02 10:00:00",
    }

    path = generator.generate(stats)

    assert path.exists()

    content = path.read_text(
        encoding="utf-8"
    )

    assert "LeetCode Sync" in content

    assert "Find Median From Data Stream" in content

    assert "Python3" in content
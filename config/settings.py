import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Config:
    BASE_DIR = BASE_DIR

    BASE_URL = "https://leetcode.com"
    GRAPHQL_URL = f"{BASE_URL}/graphql"

    LEETCODE_SESSION = os.getenv("LEETCODE_SESSION", "")
    LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME", "")
    CSRF_TOKEN = os.getenv("CSRF_TOKEN", "")

    GIT_USERNAME = os.getenv("GIT_USERNAME", "")
    GIT_EMAIL = os.getenv("GIT_EMAIL", "")

    DEBUG = False

    STORAGE_DIR = BASE_DIR / os.getenv("STORAGE_DIR", "storage")
    LOGS_DIR = BASE_DIR / os.getenv("LOGS_DIR", "logs")

    REQUEST_TIMEOUT: int = 20

    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )

    @classmethod
    def initialize(cls) -> None:
        cls.STORAGE_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOGS_DIR.mkdir(parents=True, exist_ok=True)

        (cls.STORAGE_DIR / "cache").mkdir(exist_ok=True)
        (cls.STORAGE_DIR / "submissions").mkdir(exist_ok=True)

    @classmethod
    def validate(cls):
        required = (
            "LEETCODE_SESSION",
            "LEETCODE_USERNAME",
            "CSRF_TOKEN",
        )

        for variable in required:
            if not getattr(cls, variable):
                raise ValueError(f"Missing environment variable: {variable}")

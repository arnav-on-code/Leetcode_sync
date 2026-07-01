from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

class Config:

    LEETCODE_SESSION = os.getenv("LEETCODE_SESSION", "")
    CSRF_TOKEN = os.getenv("CSRF_TOKEN", "")

    GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "")
    GITHUB_EMAIL = os.getenv("GITHUB_EMAIL", "")

    STORAGE_DIR = Path(os.getenv("STORAGE_DIR", "storage"))
    LOGS_DIR = Path(os.getenv("LOGS_DIR", "logs"))

    GRAPHQL_URL = os.getenv("GRAPHQL_URL", "https://leetcode.com/graphql")

    REQUEST_TIMEOUT = 20

    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
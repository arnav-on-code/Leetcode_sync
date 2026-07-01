from requests import Session

from config.settings import Config


class LeetCodeAuth:

    def __init__(self):
        self.session = Session()

        self.session.headers.update(
            {
                "User-Agent": Config.USER_AGENT,
                "Referer": "https://leetcode.com/",
                "Origin": "https://leetcode.com",
                "Content-Type": "application/json",
            }
        )

        self.session.cookies.update(
            {
                "LEETCODE_SESSION": Config.LEETCODE_SESSION,
                "csrftoken": Config.CSRF_TOKEN,
            }
        )

    def get_session(self) -> Session:
        """Return the configured session."""
        return self.session
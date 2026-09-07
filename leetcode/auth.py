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
                "Accept": "application/json",
            }
        )

        # Authentication cookies
        if Config.LEETCODE_SESSION:
            self.session.cookies.set(
                "LEETCODE_SESSION", Config.LEETCODE_SESSION, domain=".leetcode.com"
            )

        if Config.CSRF_TOKEN:
            self.session.cookies.set(
                "csrftoken", Config.CSRF_TOKEN, domain=".leetcode.com"
            )

    def get_session(self) -> Session:
        return self.session

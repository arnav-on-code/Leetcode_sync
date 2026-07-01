from requests import Session

from config.settings import Config


class LeetCodeClient:
    def __init__(self, session: Session):
        self.session = session

    def post(self, query: str, variables: dict = None):
        payload = {"query": query, "variables": variables or {}}

        response = self.session.post(
            Config.GRAPHQL_URL, json=payload, timeout=Config.REQUEST_TIMEOUT
        )
        if Config.DEBUG:

            print("=" * 80)
            print("Status Code:", response.status_code)
            print(response.text)
            print("=" * 80)

        return response.json()

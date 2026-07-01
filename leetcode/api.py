from requests import Session


class LeetCodeAPI:
    def __init__(self, session: Session):
        self.session = session

    def validate_session(self) -> bool:
        response = self.session.get("https://leetcode.com/api/problems/all/")

        return response.status_code == 200
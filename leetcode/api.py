from config.settings import Config
from leetcode.parser import parse_submissions
from leetcode.queries import (
    PROFILE_QUERY,
    RECENT_SUBMISSIONS_QUERY,
)


class LeetCodeAPI:

    def __init__(self, client):
        self.client = client

    def get_profile(self):
        response = self.client.post(
            PROFILE_QUERY,
            {
                "username": Config.LEETCODE_USERNAME
            }
        )

        if "errors" in response:
            raise Exception(response["errors"])

        return response["data"]["matchedUser"]

    def get_recent_submissions(self, limit=15):

        response = self.client.post(
            RECENT_SUBMISSIONS_QUERY,
            {
                "username": Config.LEETCODE_USERNAME,
                "limit": limit,
            },
        )

        if "errors" in response:
            raise Exception(response["errors"])

        return parse_submissions(
            response["data"]["recentAcSubmissionList"]
        )
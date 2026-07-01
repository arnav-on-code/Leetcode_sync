from config.settings import Config
from leetcode.parser import parse_submission_detail, parse_submissions
from leetcode.queries import (PROFILE_QUERY, RECENT_SUBMISSIONS_QUERY,
                              SUBMISSION_DETAILS_QUERY)


class LeetCodeAPI:
    def __init__(self, client):
        self.client = client

    def get_profile(self):
        """Fetch the user's profile and solved statistics."""

        response = self.client.post(
            PROFILE_QUERY,
            {"username": Config.LEETCODE_USERNAME},
        )

        if "errors" in response:
            raise Exception(response["errors"])

        return response["data"]["matchedUser"]

    def get_recent_submissions(self, limit=15):
        """Fetch the user's recent accepted submissions."""

        response = self.client.post(
            RECENT_SUBMISSIONS_QUERY,
            {
                "username": Config.LEETCODE_USERNAME,
                "limit": limit,
            },
        )

        if "errors" in response:
            raise Exception(response["errors"])

        return parse_submissions(response["data"]["recentAcSubmissionList"])

    def get_submission_detail(self, submission_id):
        """Fetch detailed information about a submission."""

        response = self.client.post(
            SUBMISSION_DETAILS_QUERY,
            {"submissionId": int(submission_id)},
        )

        if "errors" in response:
            raise Exception(response["errors"])

        return parse_submission_detail(
            submission_id,
            response["data"]["submissionDetails"],
        )

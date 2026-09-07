from config.settings import Config
from leetcode.parser import parse_submission_detail, parse_submissions
from leetcode.queries import (
    PROFILE_QUERY,
    RECENT_SUBMISSIONS_QUERY,
    SUBMISSION_DETAILS_QUERY,
)


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
    
    details = response["data"].get("submissionDetails")
    
    if details is None:
        raise Exception(
            f"LeetCode returned no submission details for submission {submission_id}"
        )
    
    return parse_submission_detail(
        submission_id,
        details,
    )

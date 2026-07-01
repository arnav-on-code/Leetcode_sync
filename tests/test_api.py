from unittest.mock import MagicMock

from leetcode.api import LeetCodeAPI


def test_get_profile():

    client = MagicMock()

    client.post.return_value = {"data": {"matchedUser": {"username": "arnav-on-code"}}}

    api = LeetCodeAPI(client)

    profile = api.get_profile()

    assert profile["username"] == "arnav-on-code"


def test_get_recent_submissions():

    client = MagicMock()

    client.post.return_value = {
        "data": {
            "recentAcSubmissionList": [
                {
                    "id": "1",
                    "title": "Two Sum",
                    "titleSlug": "two-sum",
                    "timestamp": "1780000000",
                }
            ]
        }
    }

    api = LeetCodeAPI(client)

    submissions = api.get_recent_submissions()

    assert len(submissions) == 1

    assert submissions[0].id == "1"

    assert submissions[0].title == "Two Sum"

    assert submissions[0].slug == "two-sum"


def test_get_submission_detail():

    client = MagicMock()

    client.post.return_value = {
        "data": {
            "submissionDetails": {
                "question": {
                    "questionId": "1",
                    "titleSlug": "two-sum",
                },
                "lang": {
                    "name": "python3",
                    "verboseName": "Python3",
                },
                "runtime": 45,
                "runtimeDisplay": "45 ms",
                "memory": 17000000,
                "memoryDisplay": "17 MB",
                "statusCode": 10,
                "code": "print('hello')",
                "timestamp": "1780000000",
            }
        }
    }

    api = LeetCodeAPI(client)

    detail = api.get_submission_detail("123")

    assert detail.submission_id == "123"

    assert detail.question_id == "1"

    assert detail.title_slug == "two-sum"

    assert detail.language == "python3"

    assert detail.status_code == 10

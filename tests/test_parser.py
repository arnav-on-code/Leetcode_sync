from leetcode.parser import (
    parse_submissions,
    parse_submission_detail,
)


def test_parse_submissions():

    data = [
        {
            "id": "123",
            "title": "Two Sum",
            "titleSlug": "two-sum",
            "timestamp": "1780000000",
        }
    ]

    submissions = parse_submissions(data)

    assert len(submissions) == 1

    submission = submissions[0]

    assert submission.id == "123"
    assert submission.title == "Two Sum"
    assert submission.slug == "two-sum"
    assert submission.timestamp == 1780000000


def test_parse_submission_detail():

    data = {
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

    detail = parse_submission_detail(
        "999",
        data,
    )

    assert detail.submission_id == "999"

    assert detail.question_id == "1"

    assert detail.title_slug == "two-sum"

    assert detail.language == "python3"

    assert detail.language_verbose == "Python3"

    assert detail.runtime == 45

    assert detail.runtime_display == "45 ms"

    assert detail.memory == 17000000

    assert detail.memory_display == "17 MB"

    assert detail.status_code == 10

    assert detail.code == "print('hello')"

    assert detail.timestamp == 1780000000
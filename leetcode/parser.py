from leetcode.models import Submission


def parse_submissions(data):
    submissions = []

    for item in data:
        submissions.append(
            Submission(
                id=item["id"],
                title=item["title"],
                slug=item["titleSlug"],
                timestamp=int(item["timestamp"])
            )
        )

    return submissions
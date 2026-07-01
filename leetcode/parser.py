from leetcode.models import Submission, SubmissionDetail


def parse_submissions(data):
    """Parse recent submissions."""

    submissions = []

    for item in data:
        submissions.append(
            Submission(
                id=item["id"],
                title=item["title"],
                slug=item["titleSlug"],
                timestamp=int(item["timestamp"]),
            )
        )

    return submissions


def parse_submission_detail(submission_id, data):
    """Parse GraphQL response into a SubmissionDetail object."""

    return SubmissionDetail(
        submission_id=str(submission_id),
        question_id=data["question"]["questionId"],
        title_slug=data["question"]["titleSlug"],
        language=data["lang"]["name"],
        language_verbose=data["lang"]["verboseName"],
        runtime=data["runtime"],
        runtime_display=data["runtimeDisplay"],
        memory=data["memory"],
        memory_display=data["memoryDisplay"],
        status_code=data["statusCode"],
        code=data["code"],
        timestamp=int(data["timestamp"]),
    )

def generate_commit_message(detail) -> str:
    return (
        f"feat(leetcode): solve "
        f"{detail.question_id} - "
        f"{detail.title_slug.replace('-', ' ').title()}"
    )

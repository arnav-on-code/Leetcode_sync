PROFILE_QUERY = """
query userProblemsSolved($username: String!) {
    matchedUser(username: $username) {
        username

        submitStatsGlobal {
            acSubmissionNum {
                difficulty
                count
                submissions
            }
        }
    }
}
"""


RECENT_SUBMISSIONS_QUERY = """
query recentAcSubmissions($username: String!, $limit: Int!) {
    recentAcSubmissionList(
        username: $username,
        limit: $limit
    ) {
        id
        title
        titleSlug
        timestamp
    }
}
"""
SUBMISSION_DETAILS_QUERY = """
query mySubmissionDetail($id: Int!) {
    submissionDetail(submissionId: $id) {
        id
        code
        runtime
        runtimeDisplay
        memory
        memoryDisplay
        statusCode
        timestamp

        lang {
            name
            verboseName
        }

        question {
            questionId
            titleSlug
            title
        }
    }
}
"""
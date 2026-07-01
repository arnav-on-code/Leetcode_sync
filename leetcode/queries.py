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
query submissionDetails($submissionId: Int!) {
    submissionDetails(submissionId: $submissionId) {

        runtime
        runtimeDisplay

        memory
        memoryDisplay

        code
        timestamp

        statusCode

        lang {
            name
            verboseName
        }

        question {
            questionId
            titleSlug
        }
    }
}
"""
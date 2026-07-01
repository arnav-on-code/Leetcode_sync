from sync.state import StateManager


class SubmissionDetector:

    def __init__(self):

        self.state = StateManager.load()

    def find_new(self, submissions):

        last_id = self.state["last_submission_id"]

        if last_id is None:
            return submissions

        new = []

        for submission in submissions:

            if submission.id == last_id:
                break

            new.append(submission)

        return new

    def update(self, newest_submission):

        StateManager.save(newest_submission.id)
import json

from config.settings import Config

STATE_FILE = Config.STORAGE_DIR / "state.json"


class StateManager:

    @staticmethod
    def load():

        if not STATE_FILE.exists():
            return {"last_submission_id": None}

        with open(STATE_FILE, "r") as file:
            return json.load(file)

    @staticmethod
    def save(last_submission_id):

        with open(STATE_FILE, "w") as file:
            json.dump(
                {"last_submission_id": last_submission_id},
                file,
                indent=4,
            )

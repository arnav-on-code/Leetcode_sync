import logging

from config.settings import Config


class Logger:
    """
    Application logger.
    """

    _logger = None

    @classmethod
    def get_logger(cls) -> logging.Logger:

        if cls._logger is not None:
            return cls._logger

        log_file = Config.LOGS_DIR / "sync.log"

        logger = logging.getLogger("leetcode_sync")

        logger.setLevel(logging.INFO)

        logger.propagate = False

        if logger.handlers:
            return logger

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )

        # Log to file
        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        # Log to console
        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

        cls._logger = logger

        return logger

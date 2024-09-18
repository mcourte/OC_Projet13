import logging
from sentry_sdk import capture_message


def sentry_log(error_type: str = "", error_message: str = ""):
    """log to sentry"""

    if error_type == "exception":
        logging.exception(error_message)
    elif error_type == "message":
        capture_message(error_message)
    else:
        logging.error(error_message)

import logging
from sentry_sdk import capture_message

# Utilisation d'un logger global
logger = logging.getLogger("sentry_logger")


def sentry_log(error_type: str = "", error_message: str = ""):
    """Log vers Sentry"""

    if error_type == "exception":
        logger.exception(error_message)  # Capture une exception avec trace complète
    elif error_type == "message":
        capture_message(error_message, level="info")  # Capture un message d'information
    elif error_type == "debug":
        logger.debug(error_message)  # Capture un log de debug
    elif error_type == "info":
        logger.info(error_message)  # Capture un log d'information
    elif error_type == "warning":
        logger.warning(error_message)  # Capture un log de warning
    else:
        logger.error(error_message)  # Capture un log d'erreur

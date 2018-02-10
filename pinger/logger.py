import logging
from constants import LOGGER_NAME, LOG_FORMAT

logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT)
logger = logging.getLogger(LOGGER_NAME)


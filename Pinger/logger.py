import logging


def get_logger(logger_name):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(logger_name)
    return logger



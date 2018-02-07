import time
import schedule
from Pinger.logger import get_logger
from Pinger.resource_checker import check_health
from Pinger.helper import read_data_from_file, validate_json_data


def service():
    logger = get_logger(__name__)
    logger.info('Started')
    data = read_data_from_file()
    logger.info('data read from file success')
    valid = validate_json_data(data)
    if valid:
        logger.info('data from file valid.')
        check_health(data)
    else:
        logger.error('data from file not valid!!!')


def schedule_service():
    schedule.every(10).seconds.do(service)
    while True:
        schedule.run_pending()
        time.sleep(1)

from logger import logger
from data_loader import DataLoader
from resource_checker import ResourceChecker


class Pinger:
    def __init__(self):
        self.data = None

    def __load_data(self):
        data_loader = DataLoader()
        data = data_loader.load_json()
        if data is not None:
            self.data = data
        else:
            raise Exception('Input not Valid')

    def __check_resource_status(self):
        resource_checker = ResourceChecker(data=self.data)
        resource_checker.check_resources()

    def run(self):
        logger.info("service started.")
        self.__load_data()
        self.__check_resource_status()

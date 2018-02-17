import json
import sys
from logger import logger
from constants import CONFIG_FILE_PATH as FILE_NAME


class DataLoader:
    def __init__(self):
        self.data = None
        self.is_data_valid = False

    def __read_data_from_file(self):
        """
        read data from json file and set it to self.data
        :return: None
        """
        try:
            with open(FILE_NAME, 'r') as file:
                data = json.loads(file.read())
                self.data = data
        except IOError as e:
            logger.error("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            logger.error("Unexpected error:", sys.exc_info()[0])

    def __validate_json_data(self):
        """
        validates the data read from json file
        :return: None
        """
        data = self.data
        if data is not None:
            # get links from json data
            links = self.data['links']
            # get webhook url from json data
            webhook_url = self.data['webhook_url']

            # validate link and webhook url
            link_valid = (type(links) is list) and (len(links) > 0)
            webhook_url_valid = (type(webhook_url) is str) and (len(webhook_url) > 0)
            # return validation response
            return link_valid and webhook_url_valid

        else:
            print("No data available in file")

    def load_json(self):
        """
        load the json file then validate the data and return response
        :return: links and webhook url in object if data is read successfully else None
        """
        logger.info('loading json data from file.')
        self.__read_data_from_file()
        logger.info('validating json data')
        is_valid = self.__validate_json_data()
        if is_valid:
            logger.info('data returned from load_json')
            return {
                "links": self.data['links'],
                "webhook_url": self.data['webhook_url']
            }
        else:
            logger.error('validation failed')
            return None

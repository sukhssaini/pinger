import json
import sys
from logger import logger


class DataLoader:
    def __init__(self):
        self.data = None
        self.is_data_valid = False

    def read_data_from_file(self):
        try:
            with open('data.json', 'r') as file:
                data = json.loads(file.read())
                self.data = data
        except IOError as e:
            logger.error("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            logger.error("Unexpected error:", sys.exc_info()[0])

    def validate_json_data(self):
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
        logger.info('loading json data from file.')
        self.read_data_from_file()
        logger.info('validating json data')
        is_valid = self.validate_json_data()
        if is_valid:
            logger.info('data returned from load_json')
            return {
                "links": self.data['links'],
                "webhook_url": self.data['webhook_url']
            }
        else:
            logger.error('validation failed')
            return None

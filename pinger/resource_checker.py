import requests
from logger import logger


# pending implementation of hitting webhook on error
class ResourceChecker:
    def __init__(self, data):
        self.links = data['links']
        self.webhook_url = data['webhook_url']

    def __check_resource(self, link):
        """
            checks the given link status
            :returns True  : if response is 200
            :returns False : if response is not 200
        """
        logger.info('checking link status {0}'.format(link))
        request = requests.get(link)
        if request.status_code == 200:
            return True
        else:
            return False

    def check_resources(self):
        """
        takes list of resources to check health.
        :return: None
        """
        if (self.links is not None) and (len(self.links) > 0):
            for link in self.links:
                status_ok = self.__check_resource(link)
                if status_ok:
                    logger.info("'{0}' link is healthy.".format(link))
                else:
                    logger.error("'{0}' link is not healthy.".format(link))
        else:
            logger.info("No health check links found.")

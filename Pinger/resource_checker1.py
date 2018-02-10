import requests
from logger import logger


# pending implementation of hitting webhook on error
class ResourceChecker:
    def __init__(self):
        self.links = None
        self.webhook_url = None

    def check_resource(self, link):
        logger.info('checking link status {0}'.format(link))
        request = requests.get(link)
        if request.status_code == 200:
            return True
        else:
            return False

    def check_resources(self):
        if (self.links is not None) and (len(self.links) > 0):
            for link in self.links:
                status_ok = self.check_resource(link)
                if status_ok:
                    logger.info("'{0}' link is healthy.".format(link))
                else:
                    logger.error("'{0}' link is not healthy.".format(link))
        else:
            logger.info("No health check links found.")

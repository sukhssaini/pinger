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
            returns tuple with
            :returns True, status_code  : if response is 200
            :returns False, status_code : if response is not 200
        """
        logger.info('checking link status {0}'.format(link))
        request = requests.get(link)
        if request.status_code == 200:
            return True, request.status_code
        else:
            return False, request.status_code

    def check_resources(self):
        """
        iterate over links for status check
        :return: None
        """
        if (self.links is not None) and (len(self.links) > 0):
            for link in self.links:
                is_healthy, status_code = self.__check_resource(link)
                if is_healthy:
                    logger.info("'{0}' link is healthy.".format(link))
                else:
                    self.webhook_execution(link, status_code)
                    logger.error("'{0}' link is not healthy.".format(link))
        else:
            logger.info("No health check links found.")

    def webhook_execution(self, link, status_code):
        """
        hit the webhook url with post request

        takes arguments :
            link : unhealthy_link,
            status_code : status code received on hitting unhealthy link

        payload of post request :
        {
            unhealthy_url : "",
            status_code : ""
        }
        :return: None
        """
        logger.info('executing webhook url for link : "{0}"'.format(link))
        payload = {
            "unhealthy_url": link,
            "status_code": status_code
        }
        request = requests.post(self.webhook_url, data=payload)
        if request.status_code == 200:
            logger.info('webhook_url post success for link : "{0}"'.format(link))
        else:
            logger.error('error while hitting webhook for link : "{0}"'.format(link))

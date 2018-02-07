import json
from urllib.parse import urlparse


def read_data_from_file():
    file = open('data.json', 'r')
    data = json.loads(file.read())
    return data


def validate_json_data(links):
    if type(links) == list:
        length = len(links)
        if length > 0:
            for link in links:
                url = urlparse(link)
                if not bool(url.scheme):
                    return False
            return True
    return False

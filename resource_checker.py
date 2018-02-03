import requests


def ping_link(link):
    request = requests.get(link)
    if request.status_code == 200:
        return True
    else:
        return False


def check_health(links):
    for link in links:
        is_live = ping_link(link)
        print("{0} link status isActive {1}".format(link, is_live))

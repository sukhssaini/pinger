import time
import schedule
from pinger import Pinger


def service():
    app = Pinger()
    app.run()


def schedule_service():
    schedule.every(10).seconds.do(service)
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule_service()

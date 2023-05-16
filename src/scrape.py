import datetime
import time

import requests

PERIOD_SECONDS = 120
URL_WAITING_TIME = "https://dxp-fds.flughafen-zuerich.ch/WaitingTimes"
URL_TIMESTAMP = "http://worldtimeapi.org/api/timezone/Europe/Zurich"
OUTPUT_FILE = "results.txt"


def scrape_record():
    timestamp_response = requests.get(URL_TIMESTAMP)
    timestamp = timestamp_response.json()["datetime"]
    formatted_timestamp = datetime.datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    headers = {"user-agent": "Mozilla"}
    waiting_time_response = requests.get(URL_WAITING_TIME, headers=headers)
    waiting_time = waiting_time_response.json()["maxWaitingTime"]
    return formatted_timestamp + " | " + waiting_time + " Minutes"


print("Starting the scraping")
while True:
    record = scrape_record()
    with open(OUTPUT_FILE, "a") as f:
        f.write(record)
    time.sleep(PERIOD_SECONDS)

import atexit
import datetime
import io

import matplotlib.pyplot as plt
import pandas as pd
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, send_file

PERIOD_SECONDS = 10
URL_WAITING_TIME = "https://dxp-fds.flughafen-zuerich.ch/WaitingTimes"
URL_TIMESTAMP = "http://worldtimeapi.org/api/timezone/Europe/Zurich"
OUTPUT_FILE = "results.txt"


def fetch_record():
    timestamp_response = requests.get(URL_TIMESTAMP)
    timestamp = timestamp_response.json()["datetime"]
    formatted_timestamp = datetime.datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/113.0.0.0 Safari/537.36"
    }
    waiting_time_response = requests.get(URL_WAITING_TIME, headers=headers)
    waiting_time = waiting_time_response.json()["maxWaitingTime"]
    return formatted_timestamp + " | " + waiting_time + " Minutes"


def write_record(record):
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{record}\n")


def scrape():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp}: Scraping a new record...")
    record = fetch_record()
    write_record(record)


app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

scheduler.add_job(scrape, "interval", seconds=PERIOD_SECONDS)


@app.route("/", methods=["GET"])
def plot_endpoint():
    df = pd.read_csv("results.txt", sep="|", header=None, names=["Timestamp", "Duration"])

    df["Timestamp"] = df["Timestamp"].str.strip()
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%Y-%m-%d %H:%M:%S")

    df["Duration"] = df["Duration"].str.strip().str.split(" ").str[0]
    df["Duration"] = [
        int(val) if "-" not in val else (int(val.split("-")[0]) + int(val.split("-")[1])) // 2 for val in df["Duration"]
    ]

    plt.plot(df["Timestamp"], df["Duration"])
    plt.xlabel("Time")
    plt.ylabel("Duration (Minutes)")
    plt.title("Waiting time at Zurich Airport")

    # Save the plot to a BytesIO buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    # Return the plot as a response
    return send_file(buffer, mimetype="image/png")


if __name__ == "__main__":
    app.run()

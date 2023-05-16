import requests

URL = "https://dxp-fds.flughafen-zuerich.ch/WaitingTimes"

headers = {"user-agent": "Mozilla"}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the maxWaitingTime value
    max_waiting_time = data["maxWaitingTime"]

    # Print the extracted value
    print(max_waiting_time)
else:
    print("Error: Failed to retrieve data from the endpoint")

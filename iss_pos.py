import requests

MY_LAT = 51.507351
MY_LONG = -0.127758

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
print(f"{longitude} - {latitude}")

timestamp = response.json()["timestamp"]
print(timestamp)


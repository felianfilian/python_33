import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
print(f"{longitude} - {latitude}")

timestamp = response.json()["timestamp"]
print(timestamp)


response02 = requests.get(url="https://api.open-meteo.com/v1/dwd-icon?latitude=52.52&longitude=13.41&hourly=temperature_2m")
elevation = response.json()["elevation"]
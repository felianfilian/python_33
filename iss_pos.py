import requests

MY_LAT = 51.5073
MY_LONG = -0.1277

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
print(f"{longitude} - {latitude}")

longitude = float(longitude)
latitude = float(latitude)
print(type(longitude))
print(type(MY_LONG))

if (MY_LONG > longitude - 5 and MY_LONG < longitude + 5) and (MY_LONG > latitude - 5 and MY_LONG < latitude + 5):
    print("its there")

timestamp = response.json()["timestamp"]
print(timestamp)


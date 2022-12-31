import requests

MY_LAT = 51.5073
MY_LONG = -0.1277

def is_iis_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    longitude = response.json()["iss_position"]["longitude"]
    latitude = response.json()["iss_position"]["latitude"]
    print(f"{longitude} - {latitude}")

    longitude = float(longitude)
    latitude = float(latitude)

    if MY_LONG - 5 < longitude < MY_LONG + 5  and MY_LAT - 5 < latitude < MY_LAT + 5:
        return True
    else:
        return False

timestamp = response.json()["timestamp"]
print(timestamp)


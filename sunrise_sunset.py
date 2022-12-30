import requests

response = requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"]

print(sunrise)


import requests

parameters = {
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"]
print(sunrise.split("T")[1].split(":")[0])


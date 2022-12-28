import requests

response = requests.get(url="http:// api.open-notify.org/iss_now.json")
response.raise_for_status()

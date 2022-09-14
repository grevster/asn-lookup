import requests
import os

token = os.environ['IPINFO_TOKEN']

ip = "8.8.8.8"
ipinfo = "https://ipinfo.io/"
url = ipinfo+ip
headers = {}
headers["Authorization"] = f"Bearer {token}"
resp = requests.get(url, headers=headers)

print(resp.json())
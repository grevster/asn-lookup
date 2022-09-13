import requests
import os
from requests.structures import CaseInsensitiveDict

token = os.environ['IPINFO_TOKEN']

ip = "8.8.8.8"
#token ="34c2af50f47083"
ipinfo = "https://ipinfo.io/"
url = ipinfo+ip
headers = {}
headers["Authorization"] = f"Bearer {token}"
resp = requests.get(url, headers=headers)

print(resp.json())
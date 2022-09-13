import requests
from requests.structures import CaseInsensitiveDict

ip = "8.8.8.8"
token="34c2af50f47083"

#url = "https://ipinfo.io/8.8.8.8"

ipinfo = "https://ipinfo.io/"

url = ipinfo+ip

print(url)


headers = CaseInsensitiveDict()
headers["User-Agent"] = "curl/7.68.0"
headers["Authorization"] = "Bearer {34c2af50f47083}"


resp = requests.get(url, headers=headers)

print(resp.status_code)

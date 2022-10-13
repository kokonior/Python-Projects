import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.quotable.io/random"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"


resp = requests.get(url, headers=headers)

print(resp)
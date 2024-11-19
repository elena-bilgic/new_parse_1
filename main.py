import requests
import pprint

url = "https://api.github.com"

params = {
    'q' : "html"
}
response = requests.get(url, params=params)
print(response.status_code)
response_json = response.json()
pprint.pprint(response_json)


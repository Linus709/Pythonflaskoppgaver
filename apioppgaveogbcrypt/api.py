import requests

url = "https://www.ssb.no/statbank/table/06913"
params = {
    "currrent": ""
}

response = requests.get(url, params=params)
print(response.status_code)

data = response.json()
print(f"Tempraturen i Oslo er{data['current']['']} ")
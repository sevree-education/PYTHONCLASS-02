import requests

params = {
    "q" : "AI",
    "sort" : "stars",
    "order" : "desc"
}

resp = requests.get("https://api.github.com/search/repositories", params=params)
try:
    resp.raise_for_status()
    data = resp.json()
    print(resp.url)
    print(data["total_count"])
except requests.HTTPError as e:
    print("Request Denied", e)
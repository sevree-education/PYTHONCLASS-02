import requests

#get a response from a given url
resp = requests.get("https://api.github.com")

if resp.status_code != 200:
    print("Error", resp.status_code)
else:
    print("SUCCESS")

#OR
resp = requests.get("https://api.github.com/users/sevree-education")
try:
    resp.raise_for_status()
    data = resp.json()
    print(data["login"])
    print(data["public_repos"])
except requests.HTTPError as e:
    print("Request Denied", e)
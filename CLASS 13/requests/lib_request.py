import requests

#get a response from a given url
resp = requests.get("https://api.github.com")

print(resp.status_code) #tells us the HTTP status
print(resp.headers["Content-Type"]) #dict of reponse headers
print(resp.text[:200]) #the body of the response as string
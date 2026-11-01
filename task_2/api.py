import requests
r = requests.get("https://api.github.com/users/M-Affan01")
r.raise_for_status()
data=r.json()
print(data["login"],data["public_repos"])

r = requests.get("https://api.github.com/users/EzazAzhar")
r.raise_for_status()
data=r.json()
print(data["login"],data["public_repos"])

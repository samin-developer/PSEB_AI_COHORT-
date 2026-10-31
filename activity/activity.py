import requests
r = requests.get("https://api.github.com/users/samin-developer")
r.raise_for_status()
data=r.json()
print(data["login"],data["public_repos"])
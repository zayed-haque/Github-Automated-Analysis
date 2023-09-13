import requests

def fetch_repositories(username):
    url=f"https://api.giithub.com/users/{username}/repos"
    response=requests.get(url,timeout=10)
    if response.status_code==200:
        return response.json()
    else:
        return []




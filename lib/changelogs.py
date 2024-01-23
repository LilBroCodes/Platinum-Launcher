import requests


def get_latest():
    api_url = "https://pnmgd.alwaysdata.net/api/src/changelogs.json"
    response = requests.get(api_url)
    data = response.json()
    versions = data["versions"]
    return versions[0]


def get_all():
    api_url = "https://pnmgd.alwaysdata.net/api/src/changelogs.json"
    response = requests.get(api_url)
    data = response.json()
    return data["versions"]


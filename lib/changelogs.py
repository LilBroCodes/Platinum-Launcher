import json

import requests


def get_latest():
    api_url = "https://pnmgd.alwaysdata.net/api/src/changelogs.json"
    response = requests.get(api_url)
    data = response.json()
    versions = data["versions"]
    return versions[0]


def get_all():
    try:
        api_url = "https://pnmgd.alwaysdata.net/api/src/changelogs.json"
        response = requests.get(api_url)
        data = response.json()
        for version in data["versions"]:
            version["success"] = True
    except json.JSONDecodeError as e:
        data = {
            "versions": [
                {
                    "version": "Error in changelogs.py",
                    "description": f"Failed to get changelogs, check your internet connection. ({str(e)})",
                    "success": False
                 }
            ]
        }
    return data["versions"]


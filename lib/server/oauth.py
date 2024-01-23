import requests


def login(username: str, password: str) -> dict:
    api_url = 'https://pnmgd.alwaysdata.net/api/login'
    data = {
        'username': username,
        'password': password
    }
    try:
        response = requests.post(api_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise
    except Exception as e:
        raise Exception(f"Fatal error in login request: {str(e)}")

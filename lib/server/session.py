import requests


def authenticate(authkey, url):
    data = {'authkey': authkey}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        if "<b>" in response.text:
            with open("error.html", "w") as error:
                error.write(response.text)
            raise ConnectionError("Failed to authenticate")
        else:
            return response.json()
    else:
        print("Authentication")

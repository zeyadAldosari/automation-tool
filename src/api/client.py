import requests

class Client:
    def __init__(self, base_url):
        self.base = base_url.rstrip("/")

    def login(self, username, password, expires_in_mins=None):
        url = f"{self.base}/user/login"
        payload = {"username": username, "password": password}
        if expires_in_mins:
            payload["expiresInMins"] = expires_in_mins
        return requests.post(url, json=payload)

    def me(self, token):
        url = f"{self.base}/user/me"
        headers = {"Authorization": f"Bearer {token}"}
        return requests.get(url, headers=headers)

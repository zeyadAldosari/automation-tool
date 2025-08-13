class TokenStore:
    def __init__(self):
        self.token = None

    def set(self, token):
        self.token = token

    def get(self):
        return self.token

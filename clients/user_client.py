from clients.base_client import BaseClient
from endpoints import Endpoint


class UserClient(BaseClient):
    def register_user(self, payload):
        return self.post(Endpoint.REGISTER_USER, payload)

    def authorize_user(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        return self.post(Endpoint.AUTHORIZE_USER, payload)

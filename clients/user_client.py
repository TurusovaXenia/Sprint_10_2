from clients.base_client import BaseClient
from endpoints import Endpoint


class UserClient(BaseClient):
    def register_user(self, payload):
        return self.post(Endpoint.REGISTER_USER, payload)

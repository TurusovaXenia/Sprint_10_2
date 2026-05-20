import pytest
import requests

from clients.user_client import UserClient
from endpoints import Endpoint


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture(scope="function")
def user_client(api_session):
    return UserClient(Endpoint.BASE_URL, api_session)


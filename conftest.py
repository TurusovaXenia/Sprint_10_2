import pytest
import requests

from clients.ad_client import AdClient
from clients.user_client import UserClient
from data import ad_payloads
from endpoints import Endpoint
from utils import helpers


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture(scope="function")
def user_client(api_session):
    return UserClient(Endpoint.BASE_URL, api_session)


@pytest.fixture(scope="function")
def user_setup(user_client):
    new_user_data = helpers.generate_new_user_data()
    response = user_client.register_user(new_user_data)
    res_json = response.json()
    user_id = res_json.get("user", {}).get("id")
    access_token = res_json.get("access_token", {}).get("access_token")

    setup_data = {
        "user_id": user_id,
        "email": new_user_data["email"],
        "password": new_user_data["password"],
        "access_token": access_token
    }

    return setup_data


@pytest.fixture(scope="function")
def ad_client(api_session):
    return AdClient(Endpoint.BASE_URL, api_session)


@pytest.fixture(scope="function")
def authorized_ad_client(ad_client, user_setup):
    ad_client.set_access_token(user_setup["access_token"])
    return ad_client


@pytest.fixture(scope="function")
def ad_cleanup(authorized_ad_client):
    data = {"ad_id": None}

    yield data

    ad_id = data.get("ad_id")
    if ad_id:
        authorized_ad_client.delete_ad(ad_id)


@pytest.fixture(scope="function")
def created_ad_id(authorized_ad_client):
    payload = ad_payloads.create_ad_payload()

    with ad_payloads.prepare_ad_with_image() as image_file:
        response = authorized_ad_client.create_ad(payload, files={"images": image_file})
    res_json = response.json()
    ad_id = res_json.get("id")

    yield ad_id

    if ad_id:
        authorized_ad_client.delete_ad(ad_id)


@pytest.fixture(scope="function")
def auth_context(authorized_ad_client):
    author_token = authorized_ad_client.access_token

    yield author_token

    authorized_ad_client.set_access_token(author_token)

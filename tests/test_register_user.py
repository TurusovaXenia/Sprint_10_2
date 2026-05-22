from data import ExpectedMessage, HTTPStatusCode
from utils import helpers


class TestRegisterUser:
    def test_register_user_success(self, user_client):
        new_user_data = helpers.generate_new_user_data()
        response = user_client.register_user(new_user_data)

        assert response.status_code == HTTPStatusCode.CREATED

        res_json = response.json()

        assert res_json.get("user", {}).get("email") == new_user_data["email"]
        assert res_json.get("access_token", {}).get("access_token"), "Токен не пришел или структура ответа изменилась"

    def test_register_user_duplicate_shows_error(self, user_client):
        new_user_data = helpers.generate_new_user_data()
        user_client.register_user(new_user_data)

        response = user_client.register_user(new_user_data)

        assert response.status_code == HTTPStatusCode.BAD_REQUEST

        res_json = response.json()

        assert res_json.get("statusCode") == HTTPStatusCode.BAD_REQUEST
        assert res_json.get("message") == ExpectedMessage.USER_ALREADY_EXISTS

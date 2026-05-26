from data import HTTPStatusCode


class TestAuthorizeUser:
    def test_authorize_user_success(self, user_client, user_setup):
        response = user_client.authorize_user(user_setup["email"], user_setup["password"])

        assert response.status_code == HTTPStatusCode.CREATED

        res_json = response.json()

        assert (res_json.get("user", {}).get("email") == user_setup["email"])
        assert res_json.get("token", {}).get("access_token"), \
            "Токен не пришел или структура ответа изменилась"

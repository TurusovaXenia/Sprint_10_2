from utils import helpers


class TestRegisterUser:
    def test_register_user_success(self, user_client):
        new_user_data = helpers.generate_new_user_data()
        response = user_client.register_user(new_user_data)
        res_json = response.json()

        assert response.status_code == 201
        assert res_json.get("user", {}).get("email") == new_user_data["email"]
        assert res_json.get("access_token", {}).get("access_token"), "Токен не пришел или структура ответа изменилась!"

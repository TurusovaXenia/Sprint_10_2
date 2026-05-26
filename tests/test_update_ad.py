import pytest

from data import AdImage, ad_payloads, ExpectedMessage, HTTPStatusCode
from utils import helpers


class TestUpdateAd:
    @pytest.mark.parametrize("field, patch_payload", ad_payloads.get_patch_payload())
    def test_update_ad_without_image_success(self, authorized_ad_client, created_ad_id, field, patch_payload):
        response = authorized_ad_client.update_ad(created_ad_id, patch_payload)

        assert response.status_code == HTTPStatusCode.OK

        res_json = response.json()
        cleaned_res = helpers.get_cleaned_response(res_json, patch_payload)

        assert cleaned_res == patch_payload

    def test_update_ad_with_image_success(self, authorized_ad_client, created_ad_id):
        payload = ad_payloads.create_ad_payload()

        with ad_payloads.prepare_ad_with_image(AdImage.FLOWER) as image_file:
            response = authorized_ad_client.update_ad(created_ad_id, payload, files={"images": image_file})

        assert response.status_code == HTTPStatusCode.OK
        assert AdImage.FLOWER in response.json().get("img1")

    def test_update_ad_by_stranger_forbidden(self, ad_client, created_ad_id, user_client, auth_context):
        stranger_user_data = helpers.generate_new_user_data()
        response_user = user_client.register_user(stranger_user_data)

        ad_client.set_access_token(response_user.json().get("access_token", {}).get("access_token"))

        payload = ad_payloads.create_ad_payload(name="Stranger")
        response = ad_client.update_ad(created_ad_id, payload)

        assert response.status_code == HTTPStatusCode.UNAUTHORIZED

        res_json = response.json()
        assert res_json.get("message") == ExpectedMessage.AD_NOT_FOUND_OR_FORBIDDEN

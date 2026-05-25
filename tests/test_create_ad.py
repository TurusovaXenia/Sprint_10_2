import pytest

from data import ad_payloads, AdCategory, HTTPStatusCode
from utils import helpers


class TestCreateAd:
    @pytest.mark.parametrize("category", [category for category in AdCategory],
                             ids=[f"category_{category.name.lower()}" for category in AdCategory])
    def test_create_ad_success(self, authorized_ad_client, category, ad_cleanup):
        payload = ad_payloads.create_ad_payload(category=category)

        with ad_payloads.prepare_ad_with_image(payload) as image_file:
            response = authorized_ad_client.create_ad(payload, files={"images": image_file})

        assert response.status_code == HTTPStatusCode.CREATED

        res_json = response.json()
        cleaned_res = helpers.get_cleaned_response(res_json, payload)

        ad_cleanup["ad_id"] = res_json.get("id")
        assert cleaned_res == payload

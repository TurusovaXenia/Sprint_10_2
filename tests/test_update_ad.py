import pytest

from data import ad_payloads, HTTPStatusCode


class TestUpdateAd:
    @pytest.mark.parametrize("field, patch_payload", ad_payloads.get_patch_payload())
    def test_update_ad_success(self, authorized_ad_client, created_ad, field, patch_payload):
        response = authorized_ad_client.update_ad(created_ad, patch_payload)

        assert response.status_code == HTTPStatusCode.OK

        res_json = response.json()
        cleaned_res = ({key: str(res_json[key]) for key in patch_payload if key in res_json})

        assert cleaned_res == patch_payload
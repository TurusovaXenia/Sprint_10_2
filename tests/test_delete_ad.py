from data import ad_payloads, ExpectedMessage, HTTPStatusCode


class TestDeleteAd:
    def test_delete_ad_success(self, authorized_ad_client, created_ad_id):
        response = authorized_ad_client.delete_ad(created_ad_id)

        assert response.status_code == HTTPStatusCode.OK
        assert response.json().get("message") == ExpectedMessage.AD_DELETED_SUCCESS

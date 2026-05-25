from data import ad_payloads, ExpectedMessage, HTTPStatusCode


class TestDeleteAd:
    def test_delete_ad_success(self, authorized_ad_client):
        payload = ad_payloads.create_ad_payload()

        with ad_payloads.prepare_ad_with_image() as image_file:
            response_create_ad = authorized_ad_client.create_ad(payload, files={"images": image_file})

        res_json = response_create_ad.json()
        ad_id = res_json.get("id")

        response = authorized_ad_client.delete_ad(ad_id)

        assert response.status_code == HTTPStatusCode.OK
        assert response.json().get("message") == ExpectedMessage.AD_DELETED_SUCCESS

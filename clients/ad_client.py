from requests_toolbelt.multipart.encoder import MultipartEncoder

from clients.base_client import BaseClient
from endpoints import Endpoint


class AdClient(BaseClient):
    def create_ad(self, payload, files=None, token=None):
        headers = self._get_headers(token, content_type=None)
        return self.post(Endpoint.CREATE_AD, payload, files, headers)

    def delete_ad(self, ad_id, token=None):
        headers = self._get_headers(token)
        return self.delete(Endpoint.DELETE_AD + f'/{ad_id}', headers=headers)

    def update_ad(self, ad_id, payload, files=None, token=None):
        fields = dict(payload)
        if files:
            for name, file_obj in files.items():
                fields[name] = (file_obj.name, file_obj)
        m = MultipartEncoder(fields=fields)
        headers = self._get_headers(token, content_type=m.content_type)
        return self.patch(Endpoint.UPDATE_AD + f'/{ad_id}', payload=m, headers=headers)

class BaseClient:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session
        self.access_token = None

    def set_access_token(self, access_token):
        self.access_token = access_token

    def _get_headers(self, manual_token=None, content_type="application/json"):
        target = manual_token if manual_token is not None else self.access_token

        headers = {}
        if target:
            headers["Authorization"] = target

        if content_type:
            headers["Content-Type"] = content_type
        return headers

    def post(self, url, payload, headers=None):
        return self.session.post(self.base_url + url, data=payload, headers=headers)

    def post_form(self, url, payload, headers=None, files=None):
        return self.session.post(self.base_url + url, payload=payload, files=files, headers=headers)

    def patch(self, url, payload, headers):
        return self.session.patch(self.base_url + url, data=payload, headers=headers)

    def delete(self, url, headers):
        return self.session.delete(self.base_url + url, headers=headers)

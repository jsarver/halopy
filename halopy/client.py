import requests
from halopy.config import HaloConfig


def _extract_request_params(endpoint, **kwargs):
    params = kwargs.copy()
    path_params = {k: params.pop(k) for k in list(params) if k.lower() in endpoint.path_params}
    query_params = {k: params.pop(k) for k in list(params) if k.lower() in endpoint.query_params}
    return path_params, query_params, params


class HaloClient:
    def __init__(self, config: HaloConfig):
        self.config = config
        self.session = requests.Session()
        self._authenticate()

    def _authenticate(self):
        resp = self.session.post(
            f"{self.config.base_url}/auth/token",
            data={
                "client_id": self.config.client_id,
                "client_secret": self.config.client_secret,
                "scope": self.config.scope,
                "grant_type": self.config.grant_type,
            },
        )
        resp.raise_for_status()
        token = resp.json()["access_token"]
        self.session.headers["Authorization"] = f"Bearer {token}"

    def request(self, endpoint, **kwargs):
        """
        Send a request to the API.

        Args:
            endpoint: The Endpoint object (e.g. Asset.GET, Agent.LIST).
            **kwargs: Path params, query params, and anything else (e.g. json=).
        """
        path_params, query_params, additional_kwargs = _extract_request_params(endpoint, **kwargs)
        url = endpoint.url(self.config.base_url, **path_params)
        response = self.session.request(
            method=endpoint.method,
            url=url,
            params=query_params,
            **additional_kwargs,
        )
        response.raise_for_status()
        return response

    def get(self, path_endpoint, **kwargs):
        return self.request(path_endpoint.GET, **kwargs)

    def post(self, path_endpoint, **kwargs):
        return self.request(path_endpoint.POST, **kwargs)

    def list(self, path_endpoint, **kwargs):
        return self.request(path_endpoint.LIST, **kwargs)

    def create(self, path_endpoint, **kwargs):
        return self.request(path_endpoint.CREATE, **kwargs)

    def delete(self, path_endpoint, **kwargs):
        return self.request(path_endpoint.DELETE, **kwargs)
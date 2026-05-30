import requests
from halopy.config import HaloConfig


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

    def _extract_request_params(self, path_endpoint, **kwargs):
        params = kwargs.copy()
        path_params = {k: params.pop(k) for k in kwargs if k.lower() in path_endpoint.path_params}
        query_params = {k: params.pop(k) for k in kwargs if k.lower() in path_endpoint.query_params}
        return path_params, query_params,params


    def _path_url(self,endpoint):
        return f"{self.config.base_url}{endpoint.path}"

    def request(self, path_endpoint,path_params=None,query_params=None, json=None):
        url = path_endpoint.url(self.config.base_url,**(path_params or {}))
        print(url)
        return self.session.request(method=path_endpoint.method,url=url,params=query_params,json=json)

    def get(self, path_endpoint, **kwargs):
        endpoint_method = path_endpoint.GET
        path_params, query_params ,kwargs = self._extract_request_params(endpoint_method, **kwargs)
        url = endpoint_method.url(self.config.base_url, **path_params)
        return self.session.request('GET',url=url,params=query_params,**kwargs)

    def post(self, path, **kwargs):
        return self.session.post(f"{self.config.base_url}/api{path}", **kwargs)

    def list(self,endpoint,**kwargs):
        url = endpoint.LIST.url(self.config.base_url,**kwargs)
        return self.session.get(f"{url}", **kwargs)

    def create(self,endpoint,json=None):
        url = endpoint.CREATE.url(self.config.base_url)
        return self.session.post(f"{url}", json=json)
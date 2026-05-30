import requests
from halopy.config import HaloConfig
import pprint

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

    def request(self, endpoint_method,prettyprint=False,raw=False,**kwargs):
        path_params, query_params, additional_kwargs = self._extract_request_params(endpoint_method, **kwargs)
        url = endpoint_method.url(self.config.base_url, **path_params)
        response = self.session.request(method=endpoint_method.method,url=url,params=query_params,**additional_kwargs)
        if raw:
            print(response.status_code,response.text)
        elif prettyprint:
            pprint.pprint(response.json())
            response = response.json()
        else:
            response=response.json()
        return response

    def get(self, path_endpoint, **kwargs):
        endpoint_method = path_endpoint.GET
        return self.request(endpoint_method,**kwargs)

    def post(self, path_endpoint, **kwargs):
        endpoint_method = path_endpoint.POST
        return self.request(endpoint_method, **kwargs)

    def list(self,path_endpoint,**kwargs):
        endpoint_method = path_endpoint.LIST
        return self.request(endpoint_method, **kwargs)

    def create(self,path_endpoint,json=None):
        endpoint_method = path_endpoint.CREATE
        return self.request(endpoint_method, json=json)
from functools import cache
from halopy.api.paths import Asset
from halopy.halo_globals import ASSETSTATUS_LOOKUP_ID
from halopy.api.core import list_api_request
from halopy.operations.lookup import get_lookup

@cache
def get_asset_status(client, status_id=None, status_name=None):
    statuses = get_lookup(client, lookup_id=ASSETSTATUS_LOOKUP_ID).json()
    if status_id:
       statuses = [s for s in statuses if s['id'] == status_id]
    elif status_name:
        statuses = [s for s in statuses if s['name'] == status_name]


    return statuses


def list_assets(client, assetgroup_id=None, pageinate=True, page_size=50, page_no=1, **kwargs):
    asset_list = list_api_request(client, Asset, assetgroup_id=assetgroup_id, pageinate=pageinate, page_size=page_size,
                                  page_no=page_no, **kwargs)
    return asset_list


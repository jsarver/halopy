from halopy.models import DeviceList
from halopy.paths import Asset

def extract_results_key(json_payload):
    for key, value in json_payload.items():
        if isinstance(value, list):
            return key

def extract_results_key(json_payload):
    for key, value in json_payload.items():
        if isinstance(value, list):
            return key
    return None

def list_api_request(client, object_name, pageinate=True, page_size=50, page_no=1, **kwargs):
    if not pageinate:
        return client.list(object_name, pageinate=pageinate, **kwargs).json()

    records = []
    page = page_no
    result_key = None
    while True:
        response = client.list(object_name, pageinate=pageinate, page_size=page_size, page_no=page, **kwargs).json()

        if result_key is None:
            result_key = extract_results_key(response)

        batch = response.get(result_key, []) if result_key else []

        if not batch:  # empty page -> done (exact-multiple case)
            break

        records.extend(batch)

        if len(batch) < page_size:  # short page -> last page
            break

        page += 1

    return records


def list_assets(client, assetgroup_id=None, pageinate=True, page_size=50, page_no=1, **kwargs):
    asset_list = list_api_request(client, Asset, assetgroup_id=assetgroup_id, pageinate=pageinate, page_size=page_size,
                                  page_no=page_no, **kwargs)
    return asset_list


def export_asset(device_list: DeviceList):
    pass

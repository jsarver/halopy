from halopy.api.paths import Endpoint
from halopy.client import HaloClient


def get_field_by_attribute(attr_value, fields, case_sensitive=False, attr_name="name"):
    """
    takes name of field and field array and returns a dict if found else empty dict
    """
    if case_sensitive:
        lookup = {f.get(attr_name): f for f in fields if f.get(attr_name) is not None}
    else:
        lookup = {f.get(attr_name, "").lower(): f for f in fields if f.get(attr_name) is not None}
        attr_value = attr_value.lower()
    return lookup.get(attr_value, {})


def pageination_supported(endpoint: Endpoint, method: str):
    for param in ['page_no', 'page_size', 'pageinate']:
        if param not in getattr(endpoint, method.upper()).query_params:
            return False
    return True

def _get_records(json_response):
    """
    finds name of field that has the records in json response
    :param json_response:
    :return:
    """
    result_key = _extract_records_key(json_response)
    return json_response.get(result_key, []) if result_key else []

def list_record(client: HaloClient, object_name: type[any], pageinate: bool = True, page_size: int = 50,
                page_no: int | None = None, **kwargs):
    if pageination_supported(object_name, 'LIST') and pageinate:

        if page_no:
            response = client.list(object_name, pageinate=pageinate, page_size=page_size, page_no=page_no, **kwargs).json()
            return _get_records(response)
        else:
            records = []
            page = 1

            while True:
                response = client.list(object_name, pageinate=pageinate, page_size=page_size, page_no=page,
                                       **kwargs).json()
                batch= _get_records(response)
                if not batch:
                    break
                records.extend(batch)
                if len(batch) < page_size:
                    break
                page += 1
            return records
    else:
        return client.list(object_name, **kwargs).json()


def _extract_records_key(json_payload):
    for key, value in json_payload.items():
        if isinstance(value, list):
            return key
    return None
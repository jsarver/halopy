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
    result_key=None
    for key, value in json_response.items():
        if isinstance(value, list):
            result_key= key
            break
    record_count= json_response.get('record_couht')
    records =  json_response.get(result_key, [])

    return records, record_count

def list_record(client: HaloClient, object_name: type[any], pageinate: bool = True, page_size: int = 50,
                page_no: int | None = None, **kwargs):
    if pageination_supported(object_name, 'LIST') and pageinate:

        if page_no:
            response = client.list(object_name, pageinate=pageinate, page_size=page_size, page_no=page_no, **kwargs).json()
            records, total= _get_records(response)
            return records
        else:
            records = []
            page = 1

            while True:
                response = client.list(object_name, pageinate=pageinate, page_size=page_size, page_no=page,
                                       **kwargs).json()
                batch,total= _get_records(response)
                if not batch:
                    break
                records.extend(batch)
                if total is not None and len(records) >= total:
                    break
                page += 1
            return records
    else:
        return client.list(object_name, **kwargs).json()


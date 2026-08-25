

def get_field_by_attribute(attr_value, fields, case_sensitive=False, attr_name="name"):
    """
    takes name of field and field array and returns a dict if found else empty dict
    """
    if case_sensitive:
        lookup={f.get(attr_name):f for f in fields if f.get(attr_name) is not None}
    else:
        lookup={f.get(attr_name,"").lower():f for f in fields if f.get(attr_name) is not None}
        attr_value=attr_value.lower()
    return lookup.get(attr_value, {})

def list_api_request(client, object_name, pageinate=True, page_size=50, page_no=None, **kwargs):
    if not pageinate or not page_no:
        return client.list(object_name, pageinate=pageinate,page_no=page_no, **kwargs).json()

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


def extract_results_key(json_payload):
    for key, value in json_payload.items():
        if isinstance(value, list):
            return key

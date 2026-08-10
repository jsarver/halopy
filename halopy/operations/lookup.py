from functools import cache

from halopy.api.paths import Field


@cache
def get_lookup(client,field_id,kind='T',getlookupvalues=True):
    return client.get(Field, id=field_id,kind=kind, getlookupvalues=getlookupvalues)




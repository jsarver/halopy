from functools import cache
from halopy.api.paths import Field,Lookup


@cache
def get_fieldlookup(client, field_id, kind='T', getlookupvalues=True):
    return client.get(Field, id=field_id,kind=kind, getlookupvalues=getlookupvalues)

def get_lookup(client, lookup_id=None):
    return client.list(Lookup, lookupid=lookup_id)



from functools import cache
from halopy.api.paths import Field, Lookup, Fieldinfo
from halopy.api.models import Device,DeviceView,DeviceList


@cache
def get_fieldlookup(client, field_id, kind='T', getlookupvalues=True,**kwargs):
    """

    :param client:
    :param field_id:
    :param kind:
    :param getlookupvalues:
    :return:
    """
    return client.get(Field, id=field_id,kind=kind, getlookupvalues=getlookupvalues,**kwargs)

@cache
def get_fieldinfo(client, fieldinfo_id, entityid=None, getlookupvalues=True, siteid=-1, clientid=-1, userid=-1, **kwargs):
    """
    :param client:
    :param fieldinfo_id: field id
    :param entityid:
    :param getlookupvalues:
    :param siteid:
    :param clientid:
    :param userid:
    :return:
    """
    return client.get(Fieldinfo, id=fieldinfo_id, entityid=entityid, getlookupvalues=getlookupvalues, siteid=siteid, clientid=clientid, userid=userid, **kwargs)

def get_lookup(client, lookup_id=None):
    return client.list(Lookup, lookupid=lookup_id)



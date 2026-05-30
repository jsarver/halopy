"""
Auto-generated API path constants from OpenAPI spec.
Do not edit manually — regenerate with generate_paths.py
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Endpoint:
    """Describes a single API endpoint with metadata from the OpenAPI spec."""

    path: str
    method: str
    summary: str = ""
    description: str = ""
    operation_id: str = ""
    path_params: list[str] = field(default_factory=list)
    query_params: list[str] = field(default_factory=list)
    request_model: str = ""
    response_model: str = ""

    def url(self, base: str = "", **kwargs) -> str:
        """Build full URL, formatting path params: ep.url(base, id=42)"""
        return f"{base}/api{self.path.format(**kwargs)}"


class Aisuggestion:
    CREATE = Endpoint(
        path="/AISuggestion",
        method="POST",
        request_model="AiSuggestion",
    )
    DELETE = Endpoint(
        path="/AISuggestion/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AISuggestion/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AISuggestion",
        method="GET",
    )


class Att:
    LIST = Endpoint(
        path="/ATT/PriceAndAvailability",
        method="GET",
    )


class Aws:
    LIST = Endpoint(
        path="/AWS/Get",
        method="GET",
    )


class Awsdetails:
    CREATE = Endpoint(
        path="/AWSDetails",
        method="POST",
        request_model="AWSDetails",
    )
    DELETE = Endpoint(
        path="/AWSDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AWSDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AWSDetails",
        method="GET",
    )


class Actions:
    CREATE = Endpoint(
        path="/Actions",
        method="POST",
        request_model="Actions",
        response_model="Actions",
    )
    CREATE_POST = Endpoint(
        path="/Actions/Review",
        method="POST",
        request_model="Actions",
    )
    DELETE = Endpoint(
        path="/Actions/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Actions/{id}",
        method="GET",
        summary="Get one Actions",
        description="Use this to return a single instance of Actions. Requires authentication.",
        path_params=["id"],
        query_params=["agentonly", "emailonly", "includedetails", "includeemail", "mostrecent", "nonsystem", "penultimate", "ticket_id"],
        response_model="Actions",
    )
    LIST = Endpoint(
        path="/Actions",
        method="GET",
        summary="List of Actions",
        description="Use this to return multiple Actions. Requires authentication.",
        query_params=["actoutcome", "actoutcomenum", "agentonly", "conversationonly", "count", "datesearch", "enddate", "excludebilling", "excludehiddenfrominternalit", "excludeprivate", "excludesys", "importantonly", "importanttop", "includeagentdetails", "includeattachments", "includefacebookfields", "includehtmlemail", "includehtmlnote", "includenonactionattachments", "includetranslations", "includetwitterfields", "intraticketonly", "ischildnotes", "isrelatednotes", "slaonly", "startdate", "supplieronly", "ticket_id", "timeentriesonly"],
        response_model="Actions_View",
    )


class Addigy:
    CREATE = Endpoint(
        path="/Addigy/Post",
        method="POST",
        request_model="AddigyCreateWebhook",
    )
    LIST = Endpoint(
        path="/Addigy/Get",
        method="GET",
    )


class Addigydetails:
    CREATE = Endpoint(
        path="/AddigyDetails",
        method="POST",
        request_model="AddigyDetails",
    )
    DELETE = Endpoint(
        path="/AddigyDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AddigyDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AddigyDetails",
        method="GET",
    )


class Address:
    CREATE = Endpoint(
        path="/Address",
        method="POST",
        request_model="AddressStore",
    )
    DELETE = Endpoint(
        path="/Address/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Address/{id}",
        method="GET",
        summary="Get one AddressStore",
        description="Use this to return a single instance of AddressStore. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Address",
        method="GET",
        summary="List of AddressStore",
        description="Use this to return multiple AddressStore. Requires authentication.",
        query_params=["count", "postcode", "site_id", "type_id", "user_id", "openedafter", "onholdonly", "overrideclientid", "overridesiteid", "overrideuserid"],
    )


class Addressbook:
    CREATE = Endpoint(
        path="/Addressbook",
        method="POST",
        request_model="Addressbook",
        response_model="Addressbook",
    )
    DELETE = Endpoint(
        path="/Addressbook/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Addressbook/{id}",
        method="GET",
        path_params=["id"],
        response_model="Addressbook",
    )
    LIST = Endpoint(
        path="/Addressbook",
        method="GET",
        response_model="Addressbook",
    )


class Adobeacrobatdetails:
    CREATE = Endpoint(
        path="/AdobeAcrobatDetails",
        method="POST",
        request_model="AdobeAcrobatDetails",
    )
    DELETE = Endpoint(
        path="/AdobeAcrobatDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AdobeAcrobatDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AdobeAcrobatDetails",
        method="GET",
    )


class Adobecommercedetails:
    CREATE = Endpoint(
        path="/AdobeCommerceDetails",
        method="POST",
        request_model="AdobeCommerceDetails",
    )
    DELETE = Endpoint(
        path="/AdobeCommerceDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AdobeCommerceDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AdobeCommerceDetails",
        method="GET",
    )


class Adobecommerceintegration:
    CREATE = Endpoint(
        path="/AdobeCommerceIntegration/auth",
        method="POST",
    )
    LIST = Endpoint(
        path="/AdobeCommerceIntegration",
        method="GET",
    )


class Agent:
    CREATE = Endpoint(
        path="/Agent",
        method="POST",
        request_model="Uname",
    )
    CREATE_POST = Endpoint(
        path="/Agent/ClearCache",
        method="POST",
    )
    DELETE = Endpoint(
        path="/Agent/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Agent/{id}",
        method="GET",
        summary="Get one Uname",
        description="Use this to return a single instance of Uname. Requires authentication.",
        path_params=["id"],
        query_params=["clientidoverride", "get_htmldesigner_signature", "getholidayallowance", "includedetails", "isagentconfig", "loadcache"],
    )
    LIST = Endpoint(
        path="/Agent",
        method="GET",
        summary="List of Uname",
        description="Use this to return multiple Uname. Requires authentication.",
        query_params=["activeinactive", "appointmentscreen", "basic_fields_only", "can_edit_only", "client_id", "clientidoverride", "department_id", "departments", "domain", "exchangecalendars", "exclude_membership_info", "excludeAgent", "forcequalmatch", "include_membership_info", "includeapiagents", "includedisabled", "includeenabled", "includenamedcount", "includeroles", "includestatus", "includeunassigned", "is_agent_cache", "integration_type", "linemanagedonly", "linkingagents", "loadcache", "onlinestatuses", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "qualifications", "reassign", "remoteagents", "remoteagenttype", "role", "search", "shiftagentsonly", "showall", "showcounts", "team", "team_id", "teams", "thisAgentOnly", "ticketarea_id", "tickettype_id", "view_id", "withemail"],
    )
    LIST_GET = Endpoint(
        path="/Agent/me",
        method="GET",
    )


class Agentcheckin:
    CREATE = Endpoint(
        path="/AgentCheckIn",
        method="POST",
        request_model="AgentCheckIn",
    )
    GET = Endpoint(
        path="/AgentCheckIn/{id}",
        method="GET",
        summary="Get one AgentCheckIn",
        description="Use this to return a single instance of AgentCheckIn. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/AgentCheckIn",
        method="GET",
        summary="List of AgentCheckIn",
        description="Use this to return multiple AgentCheckIn. Requires authentication.",
        query_params=["agent_id", "end_date", "start_date"],
    )


class Agenteventsubscription:
    CREATE = Endpoint(
        path="/AgentEventSubscription",
        method="POST",
        request_model="UnameEventSubscription",
    )
    DELETE = Endpoint(
        path="/AgentEventSubscription/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AgentEventSubscription/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AgentEventSubscription",
        method="GET",
    )


class Agentimage:
    GET = Endpoint(
        path="/AgentImage/{id}",
        method="GET",
        summary="Get one Uname",
        description="Use this to return a single instance of Uname. Requires authentication.",
        path_params=["id"],
        query_params=["clientidoverride", "get_htmldesigner_signature", "getholidayallowance", "includedetails", "isagentconfig", "loadcache"],
    )


class Agentpresencerule:
    LIST = Endpoint(
        path="/AgentPresenceRule",
        method="GET",
    )


class Agentpresencesubscription:
    CREATE = Endpoint(
        path="/AgentPresenceSubscription",
        method="POST",
        request_model="UnamePresenceSubscription",
    )
    DELETE = Endpoint(
        path="/AgentPresenceSubscription/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AgentPresenceSubscription/{id}",
        method="GET",
        operation_id="GetUnamePresenceSubscription",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AgentPresenceSubscription",
        method="GET",
    )


class Alemba:
    LIST = Endpoint(
        path="/Alemba/Get",
        method="GET",
    )


class Amazonsellerdetails:
    CREATE = Endpoint(
        path="/AmazonSellerDetails",
        method="POST",
        request_model="AmazonSellerDetails",
    )
    DELETE = Endpoint(
        path="/AmazonSellerDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AmazonSellerDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AmazonSellerDetails",
        method="GET",
    )


class Application:
    CREATE = Endpoint(
        path="/Application",
        method="POST",
        request_model="NHD_Identity_Application",
    )
    CREATE_POST = Endpoint(
        path="/Application/federatedcredentials",
        method="POST",
        request_model="FederatedCredential",
    )
    DELETE = Endpoint(
        path="/Application/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Application/{id}",
        method="GET",
        summary="Get one NHD_Identity_Application",
        description="Use this to return a single instance of NHD_Identity_Application. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Application",
        method="GET",
    )


class Appointment:
    CREATE = Endpoint(
        path="/Appointment",
        method="POST",
        request_model="Appointment",
    )
    CREATE_POST = Endpoint(
        path="/Appointment/Generate",
        method="POST",
    )
    DELETE = Endpoint(
        path="/Appointment/{id}",
        method="DELETE",
        summary="Delete one Appointment",
        description="Delete specific Appointment. Requires authentication.",
        path_params=["id"],
        query_params=["ignoreexchangedelete"],
    )
    GET = Endpoint(
        path="/Appointment/{id}",
        method="GET",
        summary="Get one Appointment",
        description="Use this to return a single instance of Appointment. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Appointment",
        method="GET",
        summary="List of Appointment",
        description="Use this to return multiple Appointment. Requires authentication.",
        query_params=["advanced_search", "agents", "appointmentsonly", "assets", "client_id", "end_date", "excludenonticketapptodo", "excluderecurring", "excluderecurringmaster", "getopenjourney", "hidecompleted", "includedeleted", "isrecurringchild", "isrecurringmaster", "locations", "my_approvals", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "recurringchangeonly", "recurringmasterid", "search", "shiftsonly", "showall", "showappointments", "showchanges", "showholidayonce", "showholidays", "showprojects", "showshifts", "start_date", "statuses", "tasksonly", "ticket_id", "toplevel_id", "types", "utcoffset"],
    )
    LIST_GET = Endpoint(
        path="/Appointment/Booking",
        method="GET",
    )


class Approvalprocess:
    CREATE = Endpoint(
        path="/ApprovalProcess",
        method="POST",
        request_model="ApprovalProcess",
    )
    DELETE = Endpoint(
        path="/ApprovalProcess/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ApprovalProcess/{id}",
        method="GET",
        summary="Get one ApprovalProcess",
        description="Use this to return a single instance of ApprovalProcess. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ApprovalProcess",
        method="GET",
        summary="List of ApprovalProcess",
        description="Use this to return multiple ApprovalProcess. Requires authentication.",
        query_params=["access_control_level"],
    )


class Approvalprocessrule:
    CREATE = Endpoint(
        path="/ApprovalProcessRule",
        method="POST",
        request_model="ApprovalProcessRule",
    )
    DELETE = Endpoint(
        path="/ApprovalProcessRule/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ApprovalProcessRule/{id}",
        method="GET",
        summary="Get one ApprovalProcessRule",
        description="Use this to return a single instance of ApprovalProcessRule. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ApprovalProcessRule",
        method="GET",
        summary="List of ApprovalProcessRule",
        description="Use this to return multiple ApprovalProcessRule. Requires authentication.",
        query_params=["global", "process_id", "step_id"],
    )


class Approvalstore:
    CREATE = Endpoint(
        path="/ApprovalStore",
        method="POST",
    )


class Areaazuretenant:
    LIST = Endpoint(
        path="/AreaAzureTenant",
        method="GET",
        summary="List of AreaAzureTenant",
        description="Use this to return multiple AreaAzureTenant. Requires authentication.",
        query_params=["azure_tenant_id", "client_id", "details_id", "ignore_decrypt", "notset", "returnalliflinked", "site_id"],
    )


class Arearequesttype:
    GET = Endpoint(
        path="/AreaRequestType/{id}",
        method="GET",
        summary="Get one AreaRequestType",
        description="Use this to return a single instance of AreaRequestType. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/AreaRequestType",
        method="GET",
    )


class Armis:
    LIST = Endpoint(
        path="/Armis/Get",
        method="GET",
    )


class Armisdetails:
    CREATE = Endpoint(
        path="/ArmisDetails",
        method="POST",
        request_model="ArmisDetails",
    )
    DELETE = Endpoint(
        path="/ArmisDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ArmisDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ArmisDetails",
        method="GET",
    )


class Arrowspheredetails:
    CREATE = Endpoint(
        path="/ArrowSphereDetails",
        method="POST",
        request_model="ArrowSphereDetails",
    )
    DELETE = Endpoint(
        path="/ArrowSphereDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ArrowSphereDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ArrowSphereDetails",
        method="GET",
    )


class Asset:
    CREATE = Endpoint(
        path="/Asset",
        method="POST",
        request_model="Device",
        response_model="Device",
    )
    DELETE = Endpoint(
        path="/Asset/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Asset/{id}",
        method="GET",
        summary="Get one Device",
        description="Use this to return a single instance of Device. Requires authentication.",
        path_params=["id"],
        query_params=["assettype_id", "includeactivity", "includeallowedstatus", "includedetails", "includediagramdetails", "includehierarchy"],
        response_model="Device",
    )
    LIST = Endpoint(
        path="/Asset",
        method="GET",
        summary="List of Device",
        description="Use this to return multiple Device. Requires authentication.",
        query_params=["activeinactive", "advanced_search", "assetgroup_id", "assetgroups", "assets", "assetstatuses", "assettype", "assettype_id", "assettypes", "bookmarked", "client_id", "client_ids", "columns_id", "consignable", "consignment_id", "contract_id", "contract_id_adding_to", "count", "domotzagents", "excludethese", "globalSearchID", "idonly", "includeactive", "includeallowedstatus", "includeassetfields", "includechildren", "includecolumns", "includeinactive", "includeservices", "includeuser", "integration_tenantids", "integration_type", "inventory_number", "islogonbehalfview", "item_id", "itemstock_id", "kb_id", "lastupdatefromdate", "lastupdatetodate", "licence_id", "linked_to_ticket", "linkedto_id", "mine", "mysite", "noicon", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "previously_selected", "previously_selected_client_id", "previously_selected_site_id", "previously_selected_user_id", "salesorder_id", "salesorder_line", "search", "search_inventory_number_only", "service_id", "service_ids", "site_id", "stockbin_id", "stockbin_ids", "supplier_contract_id", "supplier_id", "suppliercontracts", "ticket_id", "tickettype_id", "user_id", "username", "include_custom_fields"],
        response_model="Device_View",
    )
    LIST_GET = Endpoint(
        path="/Asset/GetAllSoftwareVersions",
        method="GET",
    )


class Assetchange:
    CREATE = Endpoint(
        path="/AssetChange",
        method="POST",
        request_model="DeviceChange",
    )
    LIST = Endpoint(
        path="/AssetChange",
        method="GET",
        summary="List of DeviceChange",
        description="Use this to return multiple DeviceChange. Requires authentication.",
        query_params=["asset_id", "count", "idonly", "licence_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "user_id"],
    )


class Assetgroup:
    CREATE = Endpoint(
        path="/AssetGroup",
        method="POST",
        request_model="Generic",
    )
    DELETE = Endpoint(
        path="/AssetGroup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AssetGroup/{id}",
        method="GET",
        summary="Get one Generic",
        description="Use this to return a single instance of Generic. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/AssetGroup",
        method="GET",
        summary="List of Generic",
        description="Use this to return multiple Generic. Requires authentication.",
        query_params=["includetypesforgroups", "istree", "type"],
    )


class Assetsoftware:
    LIST = Endpoint(
        path="/AssetSoftware",
        method="GET",
        summary="List of DeviceApplications",
        description="Use this to return multiple DeviceApplications. Requires authentication.",
        query_params=["device_id", "licence_id", "third_party_field", "third_party_id", "user_id"],
    )


class Assettype:
    CREATE = Endpoint(
        path="/AssetType",
        method="POST",
        request_model="Xtype",
    )
    DELETE = Endpoint(
        path="/AssetType/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AssetType/{id}",
        method="GET",
        summary="Get one Xtype",
        description="Use this to return a single instance of Xtype. Requires authentication.",
        path_params=["id"],
        query_params=["booking_type", "client_id", "end_date", "fieldsandlayoutonly", "includedetails", "site_id", "start_date"],
    )
    LIST = Endpoint(
        path="/AssetType",
        method="GET",
        summary="List of Xtype",
        description="Use this to return multiple Xtype. Requires authentication.",
        query_params=["assetgroup_id", "can_create_only", "can_edit_only", "fixedassetgroups", "include_current", "resourcesonly", "setuplist", "tickettype_id", "type"],
    )


class Assettypeinfo:
    LIST = Endpoint(
        path="/AssetTypeInfo",
        method="GET",
        summary="List of Xtype",
        description="Use this to return multiple Xtype. Requires authentication.",
        query_params=["assetgroup_id", "can_create_only", "can_edit_only", "fixedassetgroups", "include_current", "resourcesonly", "setuplist", "tickettype_id", "type"],
    )


class Assettypemappings:
    GET = Endpoint(
        path="/AssetTypeMappings/{id}",
        method="GET",
        summary="Get one XTypeMapping",
        description="Use this to return a single instance of XTypeMapping. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/AssetTypeMappings",
        method="GET",
    )


class Attachment:
    CREATE = Endpoint(
        path="/Attachment",
        method="POST",
        response_model="Attachment",
    )
    CREATE_POST = Endpoint(
        path="/Attachment/document",
        method="POST",
        request_model="Attachment",
    )
    DELETE = Endpoint(
        path="/Attachment/{id}",
        method="DELETE",
        path_params=["id"],
    )
    DELETE_DELETE = Endpoint(
        path="/Attachment/document/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Attachment/{id}",
        method="GET",
        summary="Get one Attachment",
        description="Use this to return a single instance of Attachment. Requires authentication.",
        path_params=["id"],
        query_params=["childticketid", "includedetails", "token"],
    )
    GET_GET = Endpoint(
        path="/Attachment/document/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Attachment",
        method="GET",
        summary="List of Attachment",
        description="Use this to return multiple Attachment. Requires authentication.",
        query_params=["action_id", "domotzagents", "filetype", "idonly", "isxlsimport", "one_attachment_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "portal", "ticket_id", "token", "type", "unique_id"],
        response_model="Attachment_View",
    )
    LIST_GET = Endpoint(
        path="/Attachment/image",
        method="GET",
        query_params=["token", "nonce"],
    )


class Audit:
    CREATE = Endpoint(
        path="/Audit",
        method="POST",
        request_model="Audit",
    )
    DELETE = Endpoint(
        path="/Audit/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Audit/{id}",
        method="GET",
        summary="Get one Audit",
        description="Use this to return a single instance of Audit. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Audit",
        method="GET",
    )


class Authinfo:
    LIST = Endpoint(
        path="/AuthInfo",
        method="GET",
    )


class Automation:
    CREATE = Endpoint(
        path="/Automation",
        method="POST",
    )
    CREATE_POST = Endpoint(
        path="/Automation/{runbookId}",
        method="POST",
        path_params=["runbookId"],
    )
    DELETE = Endpoint(
        path="/Automation/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Automation/{id}",
        method="GET",
        path_params=["id"],
        response_model="Automation",
    )
    LIST = Endpoint(
        path="/Automation",
        method="GET",
        response_model="Automation_View",
    )


class Avalaradetails:
    CREATE = Endpoint(
        path="/AvalaraDetails",
        method="POST",
        request_model="AvalaraDetails",
    )
    DELETE = Endpoint(
        path="/AvalaraDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AvalaraDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AvalaraDetails",
        method="GET",
    )


class Azuredelta:
    CREATE = Endpoint(
        path="/AzureDelta",
        method="POST",
        request_model="AzureDelta",
    )
    DELETE = Endpoint(
        path="/AzureDelta/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AzureDelta/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/AzureDelta",
        method="GET",
    )


class Azuredevopsdetails:
    CREATE = Endpoint(
        path="/AzureDevOpsDetails",
        method="POST",
        request_model="AzureDevOpsDetails",
    )
    DELETE = Endpoint(
        path="/AzureDevOpsDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/AzureDevOpsDetails/{id}",
        method="GET",
        summary="Get one AzureDevOpsDetails",
        description="Use this to return a single instance of AzureDevOpsDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/AzureDevOpsDetails",
        method="GET",
    )


class Azuretranslate:
    CREATE = Endpoint(
        path="/AzureTranslate/LanguagePackTranslate",
        method="POST",
        request_model="LanguagePack",
    )
    LIST = Endpoint(
        path="/AzureTranslate/CustomTranslate",
        method="GET",
    )


class Backgroundtask:
    GET = Endpoint(
        path="/BackgroundTask/{id}",
        method="GET",
        path_params=["id"],
    )


class Billingtemplate:
    CREATE = Endpoint(
        path="/BillingTemplate",
        method="POST",
        request_model="ContractTemplateHeader",
    )
    DELETE = Endpoint(
        path="/BillingTemplate/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/BillingTemplate/{id}",
        method="GET",
        summary="Get one ContractTemplateHeader",
        description="Use this to return a single instance of ContractTemplateHeader. Requires authentication.",
        path_params=["id"],
        query_params=["client_id", "includedetails"],
    )
    LIST = Endpoint(
        path="/BillingTemplate",
        method="GET",
    )


class Bookingtype:
    LIST = Endpoint(
        path="/BookingType",
        method="GET",
        summary="List of BookingType",
        description="Use this to return multiple BookingType. Requires authentication.",
        query_params=["type"],
    )


class Bookmark:
    CREATE = Endpoint(
        path="/Bookmark",
        method="POST",
        request_model="Bookmark",
    )
    GET = Endpoint(
        path="/Bookmark/{id}",
        method="GET",
        path_params=["id"],
    )


class Budgettype:
    CREATE = Endpoint(
        path="/BudgetType",
        method="POST",
        request_model="BudgetType",
    )
    DELETE = Endpoint(
        path="/BudgetType/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/BudgetType/{id}",
        method="GET",
        summary="Get one BudgetType",
        description="Use this to return a single instance of BudgetType. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/BudgetType",
        method="GET",
        summary="List of BudgetType",
        description="Use this to return multiple BudgetType. Requires authentication.",
        query_params=["ticket_id"],
    )


class Bulkemail:
    GET = Endpoint(
        path="/BulkEmail/{id}",
        method="GET",
        summary="Get one BulkEmail",
        description="Use this to return a single instance of BulkEmail. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/BulkEmail",
        method="GET",
    )


class Businesscentraldetails:
    CREATE = Endpoint(
        path="/BusinessCentralDetails",
        method="POST",
        request_model="BusinessCentralDetails",
    )
    DELETE = Endpoint(
        path="/BusinessCentralDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/BusinessCentralDetails/{id}",
        method="GET",
        summary="Get one BusinessCentralDetails",
        description="Use this to return a single instance of BusinessCentralDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/BusinessCentralDetails",
        method="GET",
        summary="List of BusinessCentralDetails",
        description="Use this to return multiple BusinessCentralDetails. Requires authentication.",
        query_params=["companyid", "connectedonly"],
    )


class Cab:
    CREATE = Endpoint(
        path="/CAB",
        method="POST",
        request_model="CabHeader",
    )
    DELETE = Endpoint(
        path="/CAB/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CAB/{id}",
        method="GET",
        summary="Get one CabHeader",
        description="Use this to return a single instance of CabHeader. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CAB",
        method="GET",
        summary="List of CabHeader",
        description="Use this to return multiple CabHeader. Requires authentication.",
        query_params=["includemembers"],
    )


class Cabmember:
    LIST = Endpoint(
        path="/CABMember",
        method="GET",
    )


class Cabrole:
    LIST = Endpoint(
        path="/CABRole",
        method="GET",
    )


class Crmnote:
    CREATE = Endpoint(
        path="/CRMNote",
        method="POST",
        request_model="AreaNote",
    )
    DELETE = Endpoint(
        path="/CRMNote/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CRMNote/{id}",
        method="GET",
        summary="Get one AreaNote",
        description="Use this to return a single instance of AreaNote. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CRMNote",
        method="GET",
        summary="List of AreaNote",
        description="Use this to return multiple AreaNote. Requires authentication.",
        query_params=["client_id", "count", "supplier_id", "toplevel_id"],
    )


class Cspconsumptiondata:
    CREATE = Endpoint(
        path="/CSPConsumptionData",
        method="POST",
        request_model="CSPConsumptionData",
    )
    CREATE_POST = Endpoint(
        path="/CSPConsumptionData/manage",
        method="POST",
        request_model="CSPConsumptionData",
    )
    DELETE = Endpoint(
        path="/CSPConsumptionData/{id}",
        method="DELETE",
        path_params=["id"],
    )
    DELETE_DELETE = Endpoint(
        path="/CSPConsumptionData/Parent/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CSPConsumptionData/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/CSPConsumptionData",
        method="GET",
    )


class Cspsubscriptionpricing:
    CREATE = Endpoint(
        path="/CSPSubscriptionPricing/manage",
        method="POST",
        request_model="CSPSubscriptionPricing",
    )


class Csvtemplate:
    CREATE = Endpoint(
        path="/CSVTemplate",
        method="POST",
        request_model="CSVTemplate",
    )
    DELETE = Endpoint(
        path="/CSVTemplate/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CSVTemplate/{id}",
        method="GET",
        summary="Get one CSVTemplate",
        description="Use this to return a single instance of CSVTemplate. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CSVTemplate",
        method="GET",
    )


class Calllog:
    CREATE = Endpoint(
        path="/CallLog",
        method="POST",
        request_model="CallLog",
    )
    GET = Endpoint(
        path="/CallLog/{id}",
        method="GET",
        summary="Get one CallLog",
        description="Use this to return a single instance of CallLog. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CallLog",
        method="GET",
        summary="List of CallLog",
        description="Use this to return multiple CallLog. Requires authentication.",
        query_params=["showall"],
    )


class Callscript:
    CREATE = Endpoint(
        path="/CallScript",
        method="POST",
        request_model="ScriptHeader",
    )
    DELETE = Endpoint(
        path="/CallScript/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CallScript/{id}",
        method="GET",
        summary="Get one ScriptHeader",
        description="Use this to return a single instance of ScriptHeader. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CallScript",
        method="GET",
    )


class Cannedtext:
    CREATE = Endpoint(
        path="/CannedText",
        method="POST",
        request_model="CannedText",
    )
    CREATE_POST = Endpoint(
        path="/CannedText/favourite",
        method="POST",
        request_model="CannedTextFavourites",
    )
    DELETE = Endpoint(
        path="/CannedText/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CannedText/{id}",
        method="GET",
        summary="Get one CannedText",
        description="Use this to return a single instance of CannedText. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CannedText",
        method="GET",
        summary="List of CannedText",
        description="Use this to return multiple CannedText. Requires authentication.",
        query_params=["access_control_level", "agent_id", "department_id", "group_id", "showall", "team_id", "ticketonly"],
    )


class Category:
    CREATE = Endpoint(
        path="/Category",
        method="POST",
        request_model="CategoryDetail",
    )
    DELETE = Endpoint(
        path="/Category/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Category/{id}",
        method="GET",
        summary="Get one CategoryDetail",
        description="Use this to return a single instance of CategoryDetail. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Category",
        method="GET",
        summary="List of CategoryDetail",
        description="Use this to return multiple CategoryDetail. Requires authentication.",
        query_params=["client_id", "service_id", "team_id", "team_name", "tickettype_id", "type_id"],
    )


class Certificate:
    CREATE = Endpoint(
        path="/Certificate",
        method="POST",
        request_model="Certificate",
    )
    DELETE = Endpoint(
        path="/Certificate/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Certificate/{id}",
        method="GET",
        summary="Get one Certificate",
        description="Use this to return a single instance of Certificate. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Certificate",
        method="GET",
    )


class Changecalendar:
    LIST = Endpoint(
        path="/ChangeCalendar",
        method="GET",
    )


class Chargerate:
    GET = Endpoint(
        path="/ChargeRate/{id}",
        method="GET",
        summary="Get one ChargeRate",
        description="Use this to return a single instance of ChargeRate. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ChargeRate",
        method="GET",
        summary="List of ChargeRate",
        description="Use this to return multiple ChargeRate. Requires authentication.",
        query_params=["chargerate_id", "client_id", "contract_id", "currentonly", "globalonly"],
    )


class Chat:
    CREATE = Endpoint(
        path="/Chat",
        method="POST",
    )
    GET = Endpoint(
        path="/Chat/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Chat",
        method="GET",
        summary="List of LiveChatHeader",
        description="Use this to return multiple LiveChatHeader. Requires authentication.",
        query_params=["after", "chatprofile_id", "checkavailable", "count", "ignore_all_closed", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "teams_conversation_id", "ticket_id"],
    )


class Chatflow:
    CREATE = Endpoint(
        path="/ChatFlow",
        method="POST",
        request_model="ChatFlowProcess",
    )


class Chatmatchingdata:
    CREATE = Endpoint(
        path="/ChatMatchingData",
        method="POST",
        request_model="ChatMatchingData",
    )


class Chatmessage:
    CREATE = Endpoint(
        path="/ChatMessage",
        method="POST",
        request_model="LiveChatMsg",
    )
    CREATE_POST = Endpoint(
        path="/ChatMessage/IsTyping",
        method="POST",
        request_model="LiveChatIsTyping",
    )
    LIST = Endpoint(
        path="/ChatMessage",
        method="GET",
        summary="List of LiveChatMsg",
        description="Use this to return multiple LiveChatMsg. Requires authentication.",
        query_params=["chat_id", "last_id", "max_id"],
    )


class Chatprofile:
    CREATE = Endpoint(
        path="/ChatProfile",
        method="POST",
        request_model="ChatProfile",
    )
    DELETE = Endpoint(
        path="/ChatProfile/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ChatProfile/{id}",
        method="GET",
        summary="Get one ChatProfile",
        description="Use this to return a single instance of ChatProfile. Requires authentication.",
        path_params=["id"],
        query_params=["check_available", "includedetails", "key"],
    )
    LIST = Endpoint(
        path="/ChatProfile",
        method="GET",
        summary="List of ChatProfile",
        description="Use this to return multiple ChatProfile. Requires authentication.",
        query_params=["type"],
    )


class Client:
    CREATE = Endpoint(
        path="/Client",
        method="POST",
        request_model="Area",
        response_model="Area",
    )
    CREATE_POST = Endpoint(
        path="/Client/PaymentMethodUpdate",
        method="POST",
        request_model="Area",
    )
    DELETE = Endpoint(
        path="/Client/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Client/{id}",
        method="GET",
        summary="Get one Area",
        description="Use this to return a single instance of Area. Requires authentication.",
        path_params=["id"],
        query_params=["domain", "getavailablerts", "includeactivity", "includedetails", "includeperiods", "includeprepay", "tickettype_id"],
        response_model="Area",
    )
    LIST = Endpoint(
        path="/Client",
        method="GET",
        summary="List of Area",
        description="Use this to return multiple Area. Requires authentication.",
        query_params=["accountmanageronly", "activeinactive", "advanced_search", "azureclients", "callplan", "columns_id", "count", "domain", "exclude_internal", "gficlients", "idonly", "includeactive", "includeazuretenants", "includecolumns", "includeinactive", "includeinvoicetemplatename", "includenotes", "includeqbofields", "include_custom_fields", "integration_tenantids", "integration_type", "isjira", "issentinel", "isservicenow", "lastupdatefromdate", "lastupdatetodate", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "search_name_only", "sentinelid", "showcounts", "sitefields", "snowaccountid", "snowclients", "ticketarea_id", "toplevel_id", "view_id"],
        response_model="Area_View",
    )
    LIST_GET = Endpoint(
        path="/Client/me",
        method="GET",
        response_model="Area",
    )


class Clientcache:
    LIST = Endpoint(
        path="/ClientCache",
        method="GET",
    )


class Clientcontract:
    CREATE = Endpoint(
        path="/ClientContract",
        method="POST",
        request_model="ContractHeader",
        response_model="ContractHeader",
    )
    CREATE_POST = Endpoint(
        path="/ClientContract/Approval",
        method="POST",
        request_model="ContractApproval",
    )
    DELETE = Endpoint(
        path="/ClientContract/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ClientContract/{id}",
        method="GET",
        summary="Get one ContractHeader",
        description="Use this to return a single instance of ContractHeader. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "includeperiods"],
        response_model="ContractHeader",
    )
    LIST = Endpoint(
        path="/ClientContract",
        method="GET",
        summary="List of ContractHeader",
        description="Use this to return multiple ContractHeader. Requires authentication.",
        query_params=["client_id", "count", "device_id", "excluderenewed", "includeinactive", "includelastrenewed", "isbillingplansetup", "isoracle", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "pending_recurring_invoice", "search", "site_id", "contract_type", "contract_sub_type", "labour_type"],
        response_model="ContractHeader_View",
    )


class Clientprepay:
    CREATE = Endpoint(
        path="/ClientPrepay",
        method="POST",
        request_model="PrepayHistory",
    )
    DELETE = Endpoint(
        path="/ClientPrepay/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ClientPrepay/{id}",
        method="GET",
        summary="Get one PrepayHistory",
        description="Use this to return a single instance of PrepayHistory. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ClientPrepay",
        method="GET",
        summary="List of PrepayHistory",
        description="Use this to return multiple PrepayHistory. Requires authentication.",
        query_params=["advanced_search", "billing_date", "client_id", "client_ids", "contract_id", "count", "idonly", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "ready_for_invoicing", "search"],
    )


class Configcommit:
    CREATE = Endpoint(
        path="/ConfigCommit",
        method="POST",
        request_model="ConfigCommit",
        response_model="ConfigCommit",
    )
    DELETE = Endpoint(
        path="/ConfigCommit/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ConfigCommit/{id}",
        method="GET",
        summary="Get one ConfigCommit",
        description="Use this to return a single instance of ConfigCommit. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "instance_id"],
        response_model="ConfigCommit",
    )
    LIST = Endpoint(
        path="/ConfigCommit",
        method="GET",
        summary="List of ConfigCommit",
        description="Use this to return multiple ConfigCommit. Requires authentication.",
        query_params=["advanced_search", "idonly", "instance_id", "notin_instance_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "rollback_commit", "search"],
        response_model="ConfigCommit_View",
    )


class Confirmclosure:
    CREATE = Endpoint(
        path="/ConfirmClosure",
        method="POST",
        request_model="ConfirmClosure",
    )
    DELETE = Endpoint(
        path="/ConfirmClosure/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ConfirmClosure/{id}",
        method="GET",
        summary="Get one ConfirmClosure",
        description="Use this to return a single instance of ConfirmClosure. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ConfirmClosure",
        method="GET",
    )


class Confluencedetails:
    CREATE = Endpoint(
        path="/ConfluenceDetails",
        method="POST",
        request_model="ConfluenceDetails",
    )
    DELETE = Endpoint(
        path="/ConfluenceDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ConfluenceDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ConfluenceDetails",
        method="GET",
    )


class Connectedinstance:
    CREATE = Endpoint(
        path="/ConnectedInstance",
        method="POST",
        request_model="ConnectedInstance",
    )
    DELETE = Endpoint(
        path="/ConnectedInstance/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ConnectedInstance/{id}",
        method="GET",
        summary="Get one ConnectedInstance",
        description="Use this to return a single instance of ConnectedInstance. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ConnectedInstance",
        method="GET",
    )


class Consignment:
    CREATE = Endpoint(
        path="/Consignment",
        method="POST",
        request_model="ConsignmentHeader",
    )
    DELETE = Endpoint(
        path="/Consignment/{id}",
        method="DELETE",
        path_params=["id"],
        query_params=["deleteOrder"],
    )
    GET = Endpoint(
        path="/Consignment/{id}",
        method="GET",
        summary="Get one ConsignmentHeader",
        description="Use this to return a single instance of ConsignmentHeader. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Consignment",
        method="GET",
        summary="List of ConsignmentHeader",
        description="Use this to return multiple ConsignmentHeader. Requires authentication.",
        query_params=["count", "idonly", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate"],
    )


class Contactgroup:
    CREATE = Endpoint(
        path="/Contactgroup",
        method="POST",
        request_model="Contactgroup",
    )
    DELETE = Endpoint(
        path="/Contactgroup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Contactgroup/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Contactgroup",
        method="GET",
    )


class Contactgroupcontact:
    CREATE = Endpoint(
        path="/Contactgroupcontact",
        method="POST",
        request_model="Contactgroupcontacts",
    )
    DELETE = Endpoint(
        path="/Contactgroupcontact/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Contactgroupcontact/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Contactgroupcontact",
        method="GET",
    )


class Contractrule:
    CREATE = Endpoint(
        path="/ContractRule",
        method="POST",
        request_model="ContractRule",
    )
    DELETE = Endpoint(
        path="/ContractRule/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ContractRule/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ContractRule",
        method="GET",
    )


class Contractschedule:
    CREATE = Endpoint(
        path="/ContractSchedule",
        method="POST",
        request_model="ContractSchedule",
    )
    DELETE = Endpoint(
        path="/ContractSchedule/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ContractSchedule/{id}",
        method="GET",
        summary="Get one ContractSchedule",
        description="Use this to return a single instance of ContractSchedule. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ContractSchedule",
        method="GET",
    )


class Contractscheduleplan:
    CREATE = Endpoint(
        path="/ContractSchedulePlan",
        method="POST",
        request_model="ContractSchedulePlan",
    )
    DELETE = Endpoint(
        path="/ContractSchedulePlan/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ContractSchedulePlan/{id}",
        method="GET",
        summary="Get one ContractSchedulePlan",
        description="Use this to return a single instance of ContractSchedulePlan. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ContractSchedulePlan",
        method="GET",
    )


class Control:
    CREATE = Endpoint(
        path="/Control",
        method="POST",
        request_model="Control",
    )
    CREATE_POST = Endpoint(
        path="/Control/UpdateEnc",
        method="POST",
    )
    LIST = Endpoint(
        path="/Control",
        method="GET",
        response_model="Control",
    )
    LIST_GET = Endpoint(
        path="/Control/Teams",
        method="GET",
    )


class Costcentres:
    CREATE = Endpoint(
        path="/CostCentres",
        method="POST",
        request_model="Costcentres",
    )
    DELETE = Endpoint(
        path="/CostCentres/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CostCentres/{id}",
        method="GET",
        summary="Get one Costcentres",
        description="Use this to return a single instance of Costcentres. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CostCentres",
        method="GET",
    )


class Criteriagroup:
    LIST = Endpoint(
        path="/CriteriaGroup",
        method="GET",
    )


class Currency:
    CREATE = Endpoint(
        path="/Currency",
        method="POST",
        request_model="Currency",
    )
    DELETE = Endpoint(
        path="/Currency/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Currency/{id}",
        method="GET",
        summary="Get one Currency",
        description="Use this to return a single instance of Currency. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Currency",
        method="GET",
    )


class Custombutton:
    CREATE = Endpoint(
        path="/CustomButton",
        method="POST",
        request_model="CustomButton",
    )
    DELETE = Endpoint(
        path="/CustomButton/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CustomButton/{id}",
        method="GET",
        summary="Get one CustomButton",
        description="Use this to return a single instance of CustomButton. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CustomButton",
        method="GET",
        summary="List of CustomButton",
        description="Use this to return multiple CustomButton. Requires authentication.",
        query_params=["isbuttonsetup", "ispermissionsetup", "msid", "typeid"],
    )


class Custombuttonaudit:
    CREATE = Endpoint(
        path="/CustomButtonAudit",
        method="POST",
        request_model="CustomButtonAudit",
    )


class Customintegration:
    CREATE = Endpoint(
        path="/CustomIntegration",
        method="POST",
        request_model="OutboundIntegration",
    )
    DELETE = Endpoint(
        path="/CustomIntegration/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CustomIntegration/{id}",
        method="GET",
        summary="Get one OutboundIntegration",
        description="Use this to return a single instance of OutboundIntegration. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "includemethods", "module_id"],
    )
    LIST = Endpoint(
        path="/CustomIntegration",
        method="GET",
    )


class Customintegrationmethod:
    CREATE = Endpoint(
        path="/CustomIntegrationMethod",
        method="POST",
        request_model="OutboundIntegrationMethod",
    )
    DELETE = Endpoint(
        path="/CustomIntegrationMethod/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CustomIntegrationMethod/{id}",
        method="GET",
        summary="Get one OutboundIntegrationMethod",
        description="Use this to return a single instance of OutboundIntegrationMethod. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CustomIntegrationMethod",
        method="GET",
        summary="List of OutboundIntegrationMethod",
        description="Use this to return multiple OutboundIntegrationMethod. Requires authentication.",
        query_params=["count", "integration_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate"],
    )


class Customintegrationmethodvalue:
    LIST = Endpoint(
        path="/CustomIntegrationMethodValue",
        method="GET",
    )


class Customintegrationrepository:
    GET = Endpoint(
        path="/CustomIntegrationRepository/{id}",
        method="GET",
        summary="Get one OutboundIntegration",
        description="Use this to return a single instance of OutboundIntegration. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "includemethods", "module_id"],
    )
    LIST = Endpoint(
        path="/CustomIntegrationRepository",
        method="GET",
    )


class Customquery:
    CREATE = Endpoint(
        path="/CustomQuery",
        method="POST",
        request_model="CustomQuery",
    )
    DELETE = Endpoint(
        path="/CustomQuery/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CustomQuery/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/CustomQuery",
        method="GET",
    )


class Customtable:
    CREATE = Endpoint(
        path="/CustomTable",
        method="POST",
        request_model="CustomTable",
    )
    DELETE = Endpoint(
        path="/CustomTable/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/CustomTable/{id}",
        method="GET",
        summary="Get one CustomTable",
        description="Use this to return a single instance of CustomTable. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/CustomTable",
        method="GET",
        summary="List of CustomTable",
        description="Use this to return multiple CustomTable. Requires authentication.",
        query_params=["access_control_level", "customonly", "isconfig", "iswebhookmapping", "systemonly", "usage"],
    )


class Dashboardlinks:
    CREATE = Endpoint(
        path="/DashboardLinks",
        method="POST",
        request_model="DashboardLinks",
        response_model="DashboardLinks",
    )
    DELETE = Endpoint(
        path="/DashboardLinks/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/DashboardLinks/{id}",
        method="GET",
        summary="Get one DashboardLinks",
        description="Use this to return a single instance of DashboardLinks. Requires authentication.",
        path_params=["id"],
        query_params=["getreporttoken", "includedetails", "showall", "userid"],
        response_model="DashboardLinks",
    )
    LIST = Endpoint(
        path="/DashboardLinks",
        method="GET",
        summary="List of DashboardLinks",
        description="Use this to return multiple DashboardLinks. Requires authentication.",
        query_params=["access_control_level", "count", "in_app", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "showall", "userid"],
        response_model="DashboardLinks",
    )
    LIST_GET = Endpoint(
        path="/DashboardLinks/FilterValues",
        method="GET",
    )


class Dashboardlinksrepository:
    GET = Endpoint(
        path="/DashboardLinksRepository/{id}",
        method="GET",
        summary="Get one DashboardLinks",
        description="Use this to return a single instance of DashboardLinks. Requires authentication.",
        path_params=["id"],
        query_params=["getreporttoken", "includedetails", "showall", "userid"],
    )
    LIST = Endpoint(
        path="/DashboardLinksRepository",
        method="GET",
        summary="List of DashboardLinks",
        description="Use this to return multiple DashboardLinks. Requires authentication.",
        query_params=["access_control_level", "count", "in_app", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "showall", "userid"],
    )


class Databaselookup:
    CREATE = Endpoint(
        path="/DatabaseLookup",
        method="POST",
        request_model="PartsLookup",
    )
    CREATE_POST = Endpoint(
        path="/DatabaseLookup/run",
        method="POST",
        request_model="PartsLookup",
    )
    DELETE = Endpoint(
        path="/DatabaseLookup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/DatabaseLookup/{id}",
        method="GET",
        summary="Get one PartsLookup",
        description="Use this to return a single instance of PartsLookup. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "lookup_value"],
    )
    LIST = Endpoint(
        path="/DatabaseLookup",
        method="GET",
        summary="List of PartsLookup",
        description="Use this to return multiple PartsLookup. Requires authentication.",
        query_params=["type"],
    )


class Databaselookupconfirmation:
    CREATE = Endpoint(
        path="/DatabaseLookupConfirmation",
        method="POST",
        request_model="PartsLookupConfirmation",
    )
    GET = Endpoint(
        path="/DatabaseLookupConfirmation/{id}",
        method="GET",
        path_params=["id"],
    )


class Dattocommercedetails:
    CREATE = Endpoint(
        path="/DattoCommerceDetails",
        method="POST",
        request_model="DattoCommerceDetails",
    )
    DELETE = Endpoint(
        path="/DattoCommerceDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/DattoCommerceDetails/{id}",
        method="GET",
        summary="Get one DattoCommerceDetails",
        description="Use this to return a single instance of DattoCommerceDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/DattoCommerceDetails",
        method="GET",
        summary="List of DattoCommerceDetails",
        description="Use this to return multiple DattoCommerceDetails. Requires authentication.",
        query_params=["includedetails"],
    )


class Dattormmdetails:
    CREATE = Endpoint(
        path="/DattoRmmDetails",
        method="POST",
        request_model="DattoRmmDetails",
    )
    DELETE = Endpoint(
        path="/DattoRmmDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/DattoRmmDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/DattoRmmDetails",
        method="GET",
    )


class Devicelicence:
    LIST = Endpoint(
        path="/DeviceLicence",
        method="GET",
    )


class Distributionlists:
    CREATE = Endpoint(
        path="/DistributionLists",
        method="POST",
        request_model="DistributionLists",
    )
    DELETE = Endpoint(
        path="/DistributionLists/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/DistributionLists/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/DistributionLists",
        method="GET",
    )


class Distributionlistslog:
    CREATE = Endpoint(
        path="/DistributionListsLog",
        method="POST",
        request_model="DistributionListsLog",
    )
    DELETE = Endpoint(
        path="/DistributionListsLog/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/DistributionListsLog/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/DistributionListsLog",
        method="GET",
    )


class Documentcreation:
    CREATE = Endpoint(
        path="/DocumentCreation",
        method="POST",
    )


class Downtime:
    CREATE = Endpoint(
        path="/Downtime",
        method="POST",
        request_model="Downtime",
    )
    DELETE = Endpoint(
        path="/Downtime/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Downtime/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Downtime",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/Downtime/DowntimeCalendar",
        method="GET",
    )


class Draft:
    CREATE = Endpoint(
        path="/Draft",
        method="POST",
        request_model="FaultDraft",
    )


class Dynamics365Crmdetails:
    CREATE = Endpoint(
        path="/Dynamics365CRMDetails",
        method="POST",
        request_model="Dynamics365CRMDetails",
    )
    DELETE = Endpoint(
        path="/Dynamics365CRMDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Dynamics365CRMDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Dynamics365CRMDetails",
        method="GET",
    )


class Dynatracedetails:
    CREATE = Endpoint(
        path="/DynatraceDetails",
        method="POST",
        request_model="DynatraceDetails",
    )
    DELETE = Endpoint(
        path="/DynatraceDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/DynatraceDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/DynatraceDetails",
        method="GET",
    )


class Ecommerceorder:
    CREATE = Endpoint(
        path="/EcommerceOrder",
        method="POST",
        request_model="EcommerceOrder",
    )
    DELETE = Endpoint(
        path="/EcommerceOrder/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/EcommerceOrder/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/EcommerceOrder",
        method="GET",
    )


class Emailaddressbook:
    LIST = Endpoint(
        path="/EmailAddressBook",
        method="GET",
        summary="List of Users",
        description="Use this to return multiple Users. Requires authentication.",
        query_params=["activeinactive", "advanced_search", "allapprovers", "approvers_only", "asset_id", "client_id", "contract_id", "count", "department_id", "exclude_agents", "exclude_defaultsiteusers", "exclude_generaluser", "idonly", "includeactive", "includebillinginfo", "include_custom_fields", "includeinactive", "includename", "includenonserviceaccount", "includenotes", "includeserviceaccount", "integration_type", "is_followers", "is3cxcall", "lastupdatefromdate", "lastupdatetodate", "licence_id", "listagentuserfirst", "myallcustomers", "myarea", "mydepartment", "mysite", "mysitecontact", "mytoplevel", "opp_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "organisation_id", "page_no", "page_size", "pageinate", "role", "search", "search_phonenumbers", "site_id", "supplier_id", "tickettype_id", "toplevel_id", "linked_to_user_id"],
    )


class Emailrule:
    CREATE = Endpoint(
        path="/EmailRule",
        method="POST",
        request_model="EmailRule",
    )
    DELETE = Endpoint(
        path="/EmailRule/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/EmailRule/{id}",
        method="GET",
        summary="Get one EmailRule",
        description="Use this to return a single instance of EmailRule. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/EmailRule",
        method="GET",
        summary="List of EmailRule",
        description="Use this to return multiple EmailRule. Requires authentication.",
        query_params=["fromaddress", "type"],
    )


class Emailstore:
    CREATE = Endpoint(
        path="/EmailStore",
        method="POST",
        request_model="EmailStore",
    )
    DELETE = Endpoint(
        path="/EmailStore/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/EmailStore/{id}",
        method="GET",
        summary="Get one EmailStore",
        description="Use this to return a single instance of EmailStore. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/EmailStore",
        method="GET",
    )


class Emailtemplate:
    CREATE = Endpoint(
        path="/EmailTemplate",
        method="POST",
        request_model="MessageContent",
    )
    CREATE_POST = Endpoint(
        path="/EmailTemplate/preview",
        method="POST",
        request_model="MessageContent",
    )
    DELETE = Endpoint(
        path="/EmailTemplate/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/EmailTemplate/{id}",
        method="GET",
        summary="Get one MessageContent",
        description="Use this to return a single instance of MessageContent. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "messagegroup"],
    )
    LIST = Endpoint(
        path="/EmailTemplate",
        method="GET",
        summary="List of MessageContent",
        description="Use this to return multiple MessageContent. Requires authentication.",
        query_params=["access_control_level", "ignore_mg", "isconfig", "messagegroup", "release_only", "portalcss"],
    )


class Emailtemplatevariable:
    CREATE = Endpoint(
        path="/EmailTemplateVariable",
        method="POST",
        request_model="MessageContentVariable",
    )
    DELETE = Endpoint(
        path="/EmailTemplateVariable/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/EmailTemplateVariable/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/EmailTemplateVariable",
        method="GET",
    )


class Eracent:
    LIST = Endpoint(
        path="/Eracent/Get",
        method="GET",
    )


class Eracentdetails:
    CREATE = Endpoint(
        path="/EracentDetails",
        method="POST",
        request_model="EracentDetails",
    )
    DELETE = Endpoint(
        path="/EracentDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/EracentDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/EracentDetails",
        method="GET",
    )


class Event:
    CREATE = Endpoint(
        path="/Event",
        method="POST",
    )
    DELETE = Endpoint(
        path="/Event/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Event/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Event",
        method="GET",
    )


class Eventrule:
    CREATE = Endpoint(
        path="/EventRule",
        method="POST",
        request_model="EventRule",
    )
    DELETE = Endpoint(
        path="/EventRule/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/EventRule/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/EventRule",
        method="GET",
    )


class Exactdetails:
    CREATE = Endpoint(
        path="/ExactDetails",
        method="POST",
        request_model="ExactDetails",
    )
    DELETE = Endpoint(
        path="/ExactDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ExactDetails/{id}",
        method="GET",
        summary="Get one ExactDetails",
        description="Use this to return a single instance of ExactDetails. Requires authentication.",
        path_params=["id"],
        query_params=["division", "includedetails"],
    )
    LIST = Endpoint(
        path="/ExactDetails",
        method="GET",
        summary="List of ExactDetails",
        description="Use this to return multiple ExactDetails. Requires authentication.",
        query_params=["connectedonly", "division"],
    )


class Example:
    LIST = Endpoint(
        path="/Example/Get",
        method="GET",
    )


class Expense:
    CREATE = Endpoint(
        path="/Expense",
        method="POST",
        request_model="Expense",
    )
    LIST = Endpoint(
        path="/Expense",
        method="GET",
    )


class Externalchatmessage:
    CREATE = Endpoint(
        path="/ExternalChatMessage",
        method="POST",
        request_model="TeamsChatMessage_List",
    )
    DELETE = Endpoint(
        path="/ExternalChatMessage/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ExternalChatMessage/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ExternalChatMessage",
        method="GET",
    )


class Externallink:
    CREATE = Endpoint(
        path="/ExternalLink",
        method="POST",
        request_model="ExternalLink_List",
    )
    CREATE_POST = Endpoint(
        path="/ExternalLink/Generate",
        method="POST",
        request_model="GenerateExternalLink",
    )
    DELETE = Endpoint(
        path="/ExternalLink/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ExternalLink/{id}",
        method="GET",
        summary="Get one ExternalLink",
        description="Use this to return a single instance of ExternalLink. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ExternalLink",
        method="GET",
        summary="List of ExternalLink",
        description="Use this to return multiple ExternalLink. Requires authentication.",
        query_params=["count", "details_id", "halo_id", "module_id", "module_list", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "table_id", "third_party_desc", "third_party_id", "third_party_secondary_id", "third_party_type"],
    )


class Faqlists:
    CREATE = Endpoint(
        path="/FAQLists",
        method="POST",
        request_model="FAQListHead",
    )
    DELETE = Endpoint(
        path="/FAQLists/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/FAQLists/{id}",
        method="GET",
        summary="Get one FAQListHead",
        description="Use this to return a single instance of FAQListHead. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "organisation_id"],
    )
    LIST = Endpoint(
        path="/FAQLists",
        method="GET",
        summary="List of FAQListHead",
        description="Use this to return multiple FAQListHead. Requires authentication.",
        query_params=["allgroups", "endoftreeonly", "level", "organisation_id", "parent_id", "showcounts", "type"],
    )


class Facebookdetails:
    CREATE = Endpoint(
        path="/FacebookDetails",
        method="POST",
        request_model="FacebookDetails",
    )
    DELETE = Endpoint(
        path="/FacebookDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/FacebookDetails/{id}",
        method="GET",
        summary="Get one FacebookDetails",
        description="Use this to return a single instance of FacebookDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/FacebookDetails",
        method="GET",
        summary="List of FacebookDetails",
        description="Use this to return multiple FacebookDetails. Requires authentication.",
        query_params=["page_id"],
    )


class Faultviewlog:
    LIST = Endpoint(
        path="/FaultViewLog",
        method="GET",
    )


class Faultsforecasting:
    CREATE = Endpoint(
        path="/FaultsForecasting",
        method="POST",
        request_model="FaultsForecasting",
    )
    GET = Endpoint(
        path="/FaultsForecasting/{id}",
        method="GET",
        summary="Get one FaultsForecasting",
        description="Use this to return a single instance of FaultsForecasting. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )


class Features:
    CREATE = Endpoint(
        path="/Features",
        method="POST",
        request_model="ModuleSetup",
    )
    GET = Endpoint(
        path="/Features/{id}",
        method="GET",
        summary="Get one ModuleSetup",
        description="Use this to return a single instance of ModuleSetup. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Features",
        method="GET",
        summary="List of ModuleSetup",
        description="Use this to return multiple ModuleSetup. Requires authentication.",
        query_params=["isconfig", "showdisabled", "showenabled"],
    )


class Feed:
    LIST = Endpoint(
        path="/Feed",
        method="GET",
        summary="List of Feed",
        description="Use this to return multiple Feed. Requires authentication.",
        query_params=["accountmanager_id", "agent_only", "count", "exclude_private", "followed_only", "newer_than_id", "older_than_id", "one_agent_id", "one_agents_tickets_id", "one_user_id", "related_asset_id", "related_client_id", "related_site_id", "related_user_id", "user_only"],
    )


class Feedback:
    CREATE = Endpoint(
        path="/Feedback",
        method="POST",
        request_model="Feedback",
    )
    DELETE = Endpoint(
        path="/Feedback/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Feedback/{id}",
        method="GET",
        summary="Get one Feedback",
        description="Use this to return a single instance of Feedback. Requires authentication.",
        path_params=["id"],
        query_params=["clearcomment", "includedetails", "key"],
    )
    LIST = Endpoint(
        path="/Feedback",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/Feedback/FeedbackMessage",
        method="GET",
    )


class Field:
    CREATE = Endpoint(
        path="/Field",
        method="POST",
        request_model="Field",
    )
    CREATE_POST = Endpoint(
        path="/Field/AddFieldToAll/{id}",
        method="POST",
        path_params=["id"],
    )
    DELETE = Endpoint(
        path="/Field/{id}",
        method="DELETE",
        summary="Delete one Field",
        description="Delete specific Field. Requires authentication.",
        path_params=["id"],
        query_params=["kind"],
    )
    GET = Endpoint(
        path="/Field/{id}",
        method="GET",
        summary="Get one Field",
        description="Use this to return a single instance of Field. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "kind"],
    )
    LIST = Endpoint(
        path="/Field",
        method="GET",
        summary="List of Field",
        description="Use this to return multiple Field. Requires authentication.",
        query_params=["kind", "type_id"],
    )


class Fieldgroup:
    CREATE = Endpoint(
        path="/FieldGroup",
        method="POST",
        request_model="FieldGroup",
    )
    DELETE = Endpoint(
        path="/FieldGroup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/FieldGroup/{id}",
        method="GET",
        summary="Get one FieldGroup",
        description="Use this to return a single instance of FieldGroup. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/FieldGroup",
        method="GET",
        summary="List of FieldGroup",
        description="Use this to return multiple FieldGroup. Requires authentication.",
        query_params=["access_control_level", "includefields", "isconfig"],
    )


class Fieldinfo:
    CREATE = Endpoint(
        path="/FieldInfo",
        method="POST",
        request_model="FieldInfo",
        response_model="FieldInfo",
    )
    DELETE = Endpoint(
        path="/FieldInfo/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/FieldInfo/{id}",
        method="GET",
        summary="Get one FieldInfo",
        description="Use this to return a single instance of FieldInfo. Requires authentication.",
        path_params=["id"],
        query_params=["entityid", "getlookupvalues", "includedetails", "livecustomfields", "userid"],
        response_model="FieldInfo",
    )
    LIST = Endpoint(
        path="/FieldInfo",
        method="GET",
        summary="List of FieldInfo",
        description="Use this to return multiple FieldInfo. Requires authentication.",
        query_params=["access_control_level", "domain", "excluderanges", "excludetables", "excludetableself", "extratype", "fieldtype", "fieldtypemultiple", "includecategories", "includedatefields", "includejirafields", "includeremotefields", "includevalues", "inputtype", "isapprovalstep", "isconfig", "iscustomfieldsetup", "systemid", "typeid"],
        response_model="FieldInfo",
    )


class Forecastdetails:
    CREATE = Endpoint(
        path="/ForecastDetails",
        method="POST",
        request_model="ForecastDetails",
    )
    DELETE = Endpoint(
        path="/ForecastDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ForecastDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ForecastDetails",
        method="GET",
    )


class Forethoughtdetails:
    CREATE = Endpoint(
        path="/ForethoughtDetails",
        method="POST",
        request_model="ForethoughtDetails",
    )
    DELETE = Endpoint(
        path="/ForethoughtDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ForethoughtDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ForethoughtDetails",
        method="GET",
    )


class Fortnoxdetails:
    CREATE = Endpoint(
        path="/FortnoxDetails",
        method="POST",
        request_model="FortnoxDetails",
    )
    DELETE = Endpoint(
        path="/FortnoxDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/FortnoxDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/FortnoxDetails",
        method="GET",
    )


class Gworkspacedetails:
    CREATE = Endpoint(
        path="/GWorkspaceDetails",
        method="POST",
        request_model="GWorkspaceDetails",
    )
    DELETE = Endpoint(
        path="/GWorkspaceDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/GWorkspaceDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/GWorkspaceDetails",
        method="GET",
    )


class Gotoresolve:
    LIST = Endpoint(
        path="/GoToResolve/Complete",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/GoToResolve/Download",
        method="GET",
    )


class Googlebusinessdetails:
    CREATE = Endpoint(
        path="/GoogleBusinessDetails",
        method="POST",
        request_model="GoogleBusinessDetails",
    )
    DELETE = Endpoint(
        path="/GoogleBusinessDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/GoogleBusinessDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/GoogleBusinessDetails",
        method="GET",
    )


class Halodeviceinfo:
    CREATE = Endpoint(
        path="/HaloDeviceInfo",
        method="POST",
        request_model="NHD_DeviceInfo",
    )
    DELETE = Endpoint(
        path="/HaloDeviceInfo/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/HaloDeviceInfo/{id}",
        method="GET",
        path_params=["id"],
    )


class Halofield:
    LIST = Endpoint(
        path="/HaloField",
        method="GET",
    )


class Halointegration:
    CREATE = Endpoint(
        path="/HaloIntegration/CreateTicket",
        method="POST",
        request_model="Faults",
    )
    CREATE_POST = Endpoint(
        path="/HaloIntegration/CreateAction",
        method="POST",
        request_model="Actions",
    )
    LIST = Endpoint(
        path="/HaloIntegration/Get",
        method="GET",
    )


class Halonews:
    CREATE = Endpoint(
        path="/HaloNews",
        method="POST",
        request_model="HaloNews",
    )
    CREATE_POST = Endpoint(
        path="/HaloNews/read",
        method="POST",
    )
    DELETE = Endpoint(
        path="/HaloNews/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/HaloNews/{id}",
        method="GET",
        summary="Get one HaloNews",
        description="Use this to return a single instance of HaloNews. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/HaloNews",
        method="GET",
    )


class Health:
    LIST = Endpoint(
        path="/Health",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/Health/Hashing",
        method="GET",
    )


class Historicalticketvolumes:
    CREATE = Endpoint(
        path="/HistoricalTicketVolumes",
        method="POST",
        request_model="HistoricalTicketVolumes",
    )
    DELETE = Endpoint(
        path="/HistoricalTicketVolumes/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/HistoricalTicketVolumes/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/HistoricalTicketVolumes",
        method="GET",
    )


class Holiday:
    CREATE = Endpoint(
        path="/Holiday",
        method="POST",
        request_model="Holidays",
    )
    DELETE = Endpoint(
        path="/Holiday/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Holiday/{id}",
        method="GET",
        summary="Get one Holidays",
        description="Use this to return a single instance of Holidays. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Holiday",
        method="GET",
        summary="List of Holidays",
        description="Use this to return multiple Holidays. Requires authentication.",
        query_params=["agent_id", "approved_only", "end_date", "entity", "include_apid", "inclusive_end", "inclusive_start", "my_approvals", "start_date", "workdayid"],
    )


class Hopewiser:
    LIST = Endpoint(
        path="/Hopewiser/Get",
        method="GET",
    )


class Islonline:
    CREATE = Endpoint(
        path="/ISLOnline/CreateLink",
        method="POST",
        request_model="Device",
    )
    LIST = Endpoint(
        path="/ISLOnline/Get",
        method="GET",
    )


class Impersonationrequest:
    CREATE = Endpoint(
        path="/ImpersonationRequest",
        method="POST",
        request_model="ImpersonationRequest",
    )


class Importcsv:
    CREATE = Endpoint(
        path="/ImportCSV",
        method="POST",
        request_model="ImportCsv",
    )
    DELETE = Endpoint(
        path="/ImportCSV/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ImportCSV/{id}",
        method="GET",
        summary="Get one ImportCsv",
        description="Use this to return a single instance of ImportCsv. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ImportCSV",
        method="GET",
        summary="List of ImportCsv",
        description="Use this to return multiple ImportCsv. Requires authentication.",
        query_params=["includedetails", "type_id"],
    )


class Incomingevent:
    CREATE = Endpoint(
        path="/IncomingEvent",
        method="POST",
        request_model="IncomingEvent",
    )
    CREATE_POST = Endpoint(
        path="/IncomingEvent/Process",
        method="POST",
    )
    DELETE = Endpoint(
        path="/IncomingEvent/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/IncomingEvent/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/IncomingEvent",
        method="GET",
    )


class Incomingwebhook:
    CREATE = Endpoint(
        path="/IncomingWebhook",
        method="POST",
        request_model="IncomingWebhook",
    )
    CREATE_POST = Endpoint(
        path="/IncomingWebhook/Process",
        method="POST",
    )
    DELETE = Endpoint(
        path="/IncomingWebhook/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/IncomingWebhook/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/IncomingWebhook",
        method="GET",
    )


class Incomingwebhookattempt:
    LIST = Endpoint(
        path="/IncomingWebhookAttempt",
        method="GET",
    )


class Ingrammicrodetails:
    CREATE = Endpoint(
        path="/IngramMicroDetails",
        method="POST",
        request_model="IngramMicroDetails",
    )
    DELETE = Endpoint(
        path="/IngramMicroDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/IngramMicroDetails/{id}",
        method="GET",
        summary="Get one IngramMicroDetails",
        description="Use this to return a single instance of IngramMicroDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/IngramMicroDetails",
        method="GET",
    )


class Ingrammicroreseller:
    LIST = Endpoint(
        path="/IngramMicroReseller/Get",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/IngramMicroReseller/GetQuote",
        method="GET",
    )


class Ingrammicroresellerdetails:
    CREATE = Endpoint(
        path="/IngramMicroResellerDetails",
        method="POST",
        request_model="IngramMicroResellerDetails",
    )
    DELETE = Endpoint(
        path="/IngramMicroResellerDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/IngramMicroResellerDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/IngramMicroResellerDetails",
        method="GET",
    )


class Instance:
    CREATE = Endpoint(
        path="/Instance",
        method="POST",
        request_model="Instance",
    )
    GET = Endpoint(
        path="/Instance/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Instance",
        method="GET",
        summary="List of Instance",
        description="Use this to return multiple Instance. Requires authentication.",
        query_params=["comparewith"],
    )


class Instanceinfo:
    LIST = Endpoint(
        path="/InstanceInfo",
        method="GET",
    )


class Integrationconfiguration:
    CREATE = Endpoint(
        path="/IntegrationConfiguration",
        method="POST",
        request_model="IntegrationConfiguration",
    )
    GET = Endpoint(
        path="/IntegrationConfiguration/{id}",
        method="GET",
        summary="Get one IntegrationConfiguration",
        description="Use this to return a single instance of IntegrationConfiguration. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/IntegrationConfiguration",
        method="GET",
    )


class Integrationdata:
    CREATE = Endpoint(
        path="/IntegrationData/Import/Xero",
        method="POST",
        request_model="XeroDetails",
    )
    CREATE_POST = Endpoint(
        path="/IntegrationData/Import/Myob",
        method="POST",
        request_model="MYOBDetails",
    )
    GET = Endpoint(
        path="/IntegrationData/Get/SalesMailbox/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/IntegrationData/Get/Xero",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/IntegrationData/Get/MicrosoftSkus",
        method="GET",
    )


class Integrationdelta:
    CREATE = Endpoint(
        path="/IntegrationDelta",
        method="POST",
        request_model="IntegrationDelta",
    )
    DELETE = Endpoint(
        path="/IntegrationDelta/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/IntegrationDelta/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/IntegrationDelta",
        method="GET",
    )


class Integrationerror:
    CREATE = Endpoint(
        path="/IntegrationError",
        method="POST",
        request_model="IntegrationError",
    )
    DELETE = Endpoint(
        path="/IntegrationError/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/IntegrationError/{id}",
        method="GET",
        summary="Get one IntegrationError",
        description="Use this to return a single instance of IntegrationError. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/IntegrationError",
        method="GET",
        summary="List of IntegrationError",
        description="Use this to return multiple IntegrationError. Requires authentication.",
        query_params=["count", "detail_id", "module_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate"],
    )


class Integrationexport:
    CREATE = Endpoint(
        path="/IntegrationExport",
        method="POST",
        request_model="IntegrationExport",
    )
    DELETE = Endpoint(
        path="/IntegrationExport/{id}",
        method="DELETE",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/IntegrationExport",
        method="GET",
        summary="List of IntegrationExport",
        description="Use this to return multiple IntegrationExport. Requires authentication.",
        query_params=["moduleId", "readyForImport"],
    )


class Integrationfielddata:
    CREATE = Endpoint(
        path="/IntegrationFieldData",
        method="POST",
        request_model="IntegrationFieldData",
    )
    DELETE = Endpoint(
        path="/IntegrationFieldData/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/IntegrationFieldData/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/IntegrationFieldData",
        method="GET",
    )


class Integrationfieldmapping:
    LIST = Endpoint(
        path="/IntegrationFieldMapping",
        method="GET",
        summary="List of IntegrationFieldMapping",
        description="Use this to return multiple IntegrationFieldMapping. Requires authentication.",
        query_params=["msid", "product_id", "subtypeid", "syncfields", "typeid", "xmvalue"],
    )


class Integrationlookup:
    CREATE = Endpoint(
        path="/IntegrationLookUp",
        method="POST",
        request_model="IntegrationLookUp",
    )
    LIST = Endpoint(
        path="/IntegrationLookUp",
        method="GET",
    )


class Integrationrequest:
    CREATE = Endpoint(
        path="/IntegrationRequest",
        method="POST",
        request_model="IntegrationRequest",
    )
    DELETE = Endpoint(
        path="/IntegrationRequest/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/IntegrationRequest/{id}",
        method="GET",
        summary="Get one IntegrationRequest",
        description="Use this to return a single instance of IntegrationRequest. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/IntegrationRequest",
        method="GET",
        summary="List of IntegrationRequest",
        description="Use this to return multiple IntegrationRequest. Requires authentication.",
        query_params=["count", "detail_id", "inbound_only", "module_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "outbound_only", "page_no", "page_size", "pageinate"],
    )


class Integrationrunbookvariablegroup:
    GET = Endpoint(
        path="/IntegrationRunbookVariableGroup/{id}",
        method="GET",
        summary="Get one IntegrationRunbookVariableGroup",
        description="Use this to return a single instance of IntegrationRunbookVariableGroup. Requires authentication.",
        path_params=["id"],
        query_params=["exclude_method_id", "method_ids"],
    )
    LIST = Endpoint(
        path="/IntegrationRunbookVariableGroup",
        method="GET",
        summary="List of IntegrationRunbookVariableGroup",
        description="Use this to return multiple IntegrationRunbookVariableGroup. Requires authentication.",
        query_params=["exclude_method_id", "one_runbook_id"],
    )


class Integrationsitemapping:
    LIST = Endpoint(
        path="/IntegrationSiteMapping",
        method="GET",
        summary="List of IntegrationSiteMapping",
        description="Use this to return multiple IntegrationSiteMapping. Requires authentication.",
        query_params=["get_active_only", "msid", "third_party_client_id"],
    )


class Integratorlog:
    LIST = Endpoint(
        path="/IntegratorLog",
        method="GET",
        summary="List of IntegratorLog",
        description="Use this to return multiple IntegratorLog. Requires authentication.",
        query_params=["module_id", "page_no", "page_size", "pageinate"],
    )


class Integratorschedule:
    LIST = Endpoint(
        path="/IntegratorSchedule",
        method="GET",
        summary="List of IntegratorSchedule",
        description="Use this to return multiple IntegratorSchedule. Requires authentication.",
        query_params=["page_no", "page_size", "pageinate"],
    )


class Integratortrace:
    GET = Endpoint(
        path="/IntegratorTrace/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/IntegratorTrace",
        method="GET",
    )


class Invoice:
    CREATE = Endpoint(
        path="/Invoice",
        method="POST",
        request_model="InvoiceHeader",
        response_model="InvoiceHeader",
    )
    CREATE_POST = Endpoint(
        path="/Invoice/PDF/{id}",
        method="POST",
        path_params=["id"],
    )
    DELETE = Endpoint(
        path="/Invoice/{id}",
        method="DELETE",
        summary="Delete one InvoiceHeader",
        description="Delete specific InvoiceHeader. Requires authentication.",
        path_params=["id"],
        query_params=["bypass_accounts_sync"],
    )
    GET = Endpoint(
        path="/Invoice/{id}",
        method="GET",
        summary="Get one InvoiceHeader",
        description="Use this to return a single instance of InvoiceHeader. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
        response_model="InvoiceHeader",
    )
    LIST = Endpoint(
        path="/Invoice",
        method="GET",
        summary="List of InvoiceHeader",
        description="Use this to return multiple InvoiceHeader. Requires authentication.",
        query_params=["advanced_search", "asset_id", "awaiting_approval", "billing_date", "billingcategory_ids", "start_date", "end_date", "datesearch", "client_id", "client_ids", "contract_id", "count", "idonly", "includecredits", "includeinvoices", "includelines", "includepoinvoices", "invoicedateend", "invoicedatestart", "my_approvals", "notpostedonly", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "paymentstatuses", "postedonly", "purchaseorder_id", "quote_status", "ready_for_invoicing", "recurringinvoice_id", "reviewrequired", "rinvoice_type", "salesorder_id", "search", "sent_status", "site_id", "stripeautopaymentrequired", "ticket_id", "toplevel_id", "user_id", "third_party_id", "xero_id", "quickbooks_id", "include_linked_item_details"],
        response_model="InvoiceHeader_View",
    )
    LIST_GET = Endpoint(
        path="/Invoice/lines",
        method="GET",
        response_model="InvoiceHeader_View",
    )


class Invoicechange:
    CREATE = Endpoint(
        path="/InvoiceChange",
        method="POST",
        request_model="InvoiceChange",
    )
    LIST = Endpoint(
        path="/InvoiceChange",
        method="GET",
        summary="List of InvoiceChange",
        description="Use this to return multiple InvoiceChange. Requires authentication.",
        query_params=["count", "idonly", "invoice_id", "line_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "type_id"],
    )


class Invoicedetailprorata:
    LIST = Endpoint(
        path="/InvoiceDetailProRata",
        method="GET",
    )


class Invoicepayment:
    CREATE = Endpoint(
        path="/InvoicePayment",
        method="POST",
        request_model="InvoicePayment_List",
    )
    DELETE = Endpoint(
        path="/InvoicePayment/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/InvoicePayment/{id}",
        method="GET",
        summary="Get one InvoicePayment",
        description="Use this to return a single instance of InvoicePayment. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/InvoicePayment",
        method="GET",
        summary="List of InvoicePayment",
        description="Use this to return multiple InvoicePayment. Requires authentication.",
        query_params=["client_id", "count", "intent_id", "invoice_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search"],
    )


class Item:
    CREATE = Endpoint(
        path="/Item",
        method="POST",
        request_model="Item",
    )
    CREATE_POST = Endpoint(
        path="/Item/NewAccountsId",
        method="POST",
        request_model="Item",
    )
    DELETE = Endpoint(
        path="/Item/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Item/{id}",
        method="GET",
        summary="Get one Item",
        description="Use this to return a single instance of Item. Requires authentication.",
        path_params=["id"],
        query_params=["dbc_company_id", "includedetails", "kashflowtenantid", "qbocompanyid", "sagebusinesscloudtenantid", "xerotenantid"],
    )
    LIST = Endpoint(
        path="/Item",
        method="GET",
        summary="List of Item",
        description="Use this to return multiple Item. Requires authentication.",
        query_params=["activeinactive", "advanced_search", "assetgroup_id", "assetgroups", "assettypes", "autotask_service_items", "count", "dbc_company_id", "exactdivision", "excluderecurring", "includeactive", "includeinactive", "include_custom_fields", "itemservice_id", "itemservicerequestdetails_id", "itemsupplierclientid", "itemsuppliercurrency", "kashflowtenantid", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "qbitemsonly", "qbocompanyid", "recurringonly", "sagebusinesscloudtenantid", "search", "search1", "show_not_in_stock", "stocklocation_id", "supplier_id", "xerotenantid"],
    )


class Itemaccountslink:
    CREATE = Endpoint(
        path="/ItemAccountsLink",
        method="POST",
        request_model="ItemAccountsLink",
    )
    CREATE_POST = Endpoint(
        path="/ItemAccountsLink/Migrate",
        method="POST",
        request_model="ItemAccountsLinkMigration",
    )
    DELETE = Endpoint(
        path="/ItemAccountsLink/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ItemAccountsLink/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ItemAccountsLink",
        method="GET",
    )


class Itemgroup:
    CREATE = Endpoint(
        path="/ItemGroup",
        method="POST",
        request_model="ItemGroup",
    )
    DELETE = Endpoint(
        path="/ItemGroup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ItemGroup/{id}",
        method="GET",
        summary="Get one ItemGroup",
        description="Use this to return a single instance of ItemGroup. Requires authentication.",
        path_params=["id"],
        query_params=["groupQuantity", "includedetails"],
    )
    LIST = Endpoint(
        path="/ItemGroup",
        method="GET",
    )


class Itemstock:
    CREATE = Endpoint(
        path="/ItemStock",
        method="POST",
        request_model="ItemStock",
    )
    DELETE = Endpoint(
        path="/ItemStock/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ItemStock/{id}",
        method="GET",
        summary="Get one ItemStock",
        description="Use this to return a single instance of ItemStock. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ItemStock",
        method="GET",
        summary="List of ItemStock",
        description="Use this to return multiple ItemStock. Requires authentication.",
        query_params=["count", "idonly", "item_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "stockbin_id", "stocklocation_id"],
    )


class Itemstockhistory:
    GET = Endpoint(
        path="/ItemStockHistory/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ItemStockHistory",
        method="GET",
        summary="List of ItemStockHistory",
        description="Use this to return multiple ItemStockHistory. Requires authentication.",
        query_params=["count", "idonly", "item_id", "itemstock_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "stockbin_id", "stocklocation_id"],
    )


class Jamfdetails:
    CREATE = Endpoint(
        path="/JamfDetails",
        method="POST",
        request_model="JamfDetails",
    )
    DELETE = Endpoint(
        path="/JamfDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/JamfDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/JamfDetails",
        method="GET",
    )


class Jiradetails:
    CREATE = Endpoint(
        path="/JiraDetails",
        method="POST",
        request_model="JiraDetails",
    )
    DELETE = Endpoint(
        path="/JiraDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/JiraDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/JiraDetails",
        method="GET",
    )


class Journey:
    CREATE = Endpoint(
        path="/Journey",
        method="POST",
        request_model="Journey",
    )
    DELETE = Endpoint(
        path="/Journey/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Journey/{id}",
        method="GET",
        summary="Get one Journey",
        description="Use this to return a single instance of Journey. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Journey",
        method="GET",
    )


class Kbarticle:
    CREATE = Endpoint(
        path="/KBArticle",
        method="POST",
        request_model="KBEntry",
        response_model="KBEntry",
    )
    CREATE_POST = Endpoint(
        path="/KBArticle/vote",
        method="POST",
        request_model="KBEntry",
    )
    DELETE = Endpoint(
        path="/KBArticle/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/KBArticle/{id}",
        method="GET",
        summary="Get one KBEntry",
        description="Use this to return a single instance of KBEntry. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "language_code", "language_override", "organisation_id"],
        response_model="KBEntry",
    )
    LIST = Endpoint(
        path="/KBArticle",
        method="GET",
        summary="List of KBEntry",
        description="Use this to return multiple KBEntry. Requires authentication.",
        query_params=["activeinactive", "advanced_search", "articletype", "client_id", "count", "device_id", "faqlists", "includeactive", "includeinactive", "key", "language_code", "language_override", "needsreview", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "organisation_id", "page_no", "page_size", "pageinate", "related_to", "related_to_ticket", "search", "site_id", "type"],
        response_model="KBEntry_View",
    )


class Kbarticleanon:
    GET = Endpoint(
        path="/KBArticleAnon/{slug}",
        method="GET",
        path_params=["slug"],
    )
    LIST = Endpoint(
        path="/KBArticleAnon",
        method="GET",
    )


class Kandji:
    LIST = Endpoint(
        path="/Kandji/Get",
        method="GET",
    )


class Kandjidetails:
    CREATE = Endpoint(
        path="/KandjiDetails",
        method="POST",
        request_model="KandjiDetails",
    )
    DELETE = Endpoint(
        path="/KandjiDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/KandjiDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/KandjiDetails",
        method="GET",
    )


class Kaseyavsax:
    CREATE = Endpoint(
        path="/KaseyaVSAX/CreateWebhook/{detailsId}",
        method="POST",
        path_params=["detailsId"],
    )
    DELETE = Endpoint(
        path="/KaseyaVSAX/DeleteWebhook/{detailsId}",
        method="DELETE",
        path_params=["detailsId"],
    )
    LIST = Endpoint(
        path="/KaseyaVSAX/Get",
        method="GET",
    )


class Kaseyavsaxdetails:
    CREATE = Endpoint(
        path="/KaseyaVSAXDetails",
        method="POST",
        request_model="KaseyaVSAXDetails",
    )
    DELETE = Endpoint(
        path="/KaseyaVSAXDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/KaseyaVSAXDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/KaseyaVSAXDetails",
        method="GET",
    )


class Kashflowdetails:
    CREATE = Endpoint(
        path="/KashflowDetails",
        method="POST",
        request_model="KashflowDetails",
    )
    DELETE = Endpoint(
        path="/KashflowDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/KashflowDetails/{id}",
        method="GET",
        summary="Get one KashflowDetails",
        description="Use this to return a single instance of KashflowDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/KashflowDetails",
        method="GET",
        summary="List of KashflowDetails",
        description="Use this to return multiple KashflowDetails. Requires authentication.",
        query_params=["includedisabled", "includeenabled", "tenantid"],
    )


class Keyvault:
    CREATE = Endpoint(
        path="/KeyVault",
        method="POST",
        request_model="KeyVault",
    )
    DELETE = Endpoint(
        path="/KeyVault/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/KeyVault/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/KeyVault",
        method="GET",
    )


class Ldapconnection:
    CREATE = Endpoint(
        path="/LDAPConnection",
        method="POST",
        request_model="LDAPConnection",
    )
    DELETE = Endpoint(
        path="/LDAPConnection/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/LDAPConnection/{id}",
        method="GET",
        summary="Get one LDAPConnection",
        description="Use this to return a single instance of LDAPConnection. Requires authentication.",
        path_params=["id"],
        query_params=["clientidoverride", "includedetails"],
    )
    LIST = Endpoint(
        path="/LDAPConnection",
        method="GET",
        summary="List of LDAPConnection",
        description="Use this to return multiple LDAPConnection. Requires authentication.",
        query_params=["clientidoverride"],
    )


class Languages:
    CREATE = Endpoint(
        path="/Languages",
        method="POST",
        request_model="LanguagePack",
    )
    DELETE = Endpoint(
        path="/Languages/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Languages/{id}",
        method="GET",
        summary="Get one LanguagePack",
        description="Use this to return a single instance of LanguagePack. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Languages",
        method="GET",
        summary="List of LanguagePack",
        description="Use this to return multiple LanguagePack. Requires authentication.",
        query_params=["showall"],
    )


class Lapsafe:
    LIST = Endpoint(
        path="/LapSafe/Get",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/LapSafe/Complete",
        method="GET",
    )


class Licencechange:
    LIST = Endpoint(
        path="/LicenceChange",
        method="GET",
        summary="List of LicenceChange",
        description="Use this to return multiple LicenceChange. Requires authentication.",
        query_params=["change_date", "count", "idonly", "licence_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search"],
    )


class Licenseinfo:
    CREATE = Endpoint(
        path="/LicenseInfo",
        method="POST",
        request_model="LicenceInfo",
    )
    LIST = Endpoint(
        path="/LicenseInfo",
        method="GET",
        summary="List of LicenceInfo",
        description="Use this to return multiple LicenceInfo. Requires authentication.",
        query_params=["advanced_search", "count", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "site_id"],
    )
    LIST_GET = Endpoint(
        path="/LicenseInfo/password",
        method="GET",
    )


class Logintoken:
    CREATE = Endpoint(
        path="/LoginToken",
        method="POST",
        request_model="LoginToken",
    )


class Lookup:
    CREATE = Endpoint(
        path="/Lookup",
        method="POST",
        request_model="Lookup",
        response_model="Lookup",
    )
    CREATE_POST = Endpoint(
        path="/Lookup/ClearCache",
        method="POST",
    )
    DELETE = Endpoint(
        path="/Lookup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Lookup/{id}",
        method="GET",
        summary="Get one Lookup",
        description="Use this to return a single instance of Lookup. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
        response_model="Lookup",
    )
    LIST = Endpoint(
        path="/Lookup",
        method="GET",
        summary="List of Lookup",
        description="Use this to return multiple Lookup. Requires authentication.",
        query_params=["access_control_level", "assettype_id", "client_id", "clientname", "contract_id", "country_code_id", "dbc_company_id", "domain", "exclude_nocharge", "exclude_nolinkedtypes", "exclude_zero", "iscustomfield", "istree", "lookupid", "ordervaluetype", "outcome_id", "showallcodes", "ticket_id", "unameaprestriction", "use", "use2"],
        response_model="Lookup",
    )


class Mo:
    CREATE = Endpoint(
        path="/MO",
        method="POST",
        request_model="MarketingOpen",
    )
    DELETE = Endpoint(
        path="/MO/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MO/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MO",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/MO/r",
        method="GET",
    )


class Myobdetails:
    CREATE = Endpoint(
        path="/MYOBdetails",
        method="POST",
        request_model="MYOBDetails",
    )
    DELETE = Endpoint(
        path="/MYOBdetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MYOBdetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MYOBdetails",
        method="GET",
    )


class Mail:
    CREATE = Endpoint(
        path="/Mail/Azure",
        method="POST",
    )
    CREATE_POST = Endpoint(
        path="/Mail/ProcessMail",
        method="POST",
        query_params=["task_id"],
    )


class Mailcampaign:
    CREATE = Endpoint(
        path="/MailCampaign",
        method="POST",
        request_model="MailCampaign",
    )
    DELETE = Endpoint(
        path="/MailCampaign/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MailCampaign/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MailCampaign",
        method="GET",
    )


class Mailcampaignemail:
    CREATE = Endpoint(
        path="/MailCampaignEmail",
        method="POST",
        request_model="MailCampaignEmail",
    )
    DELETE = Endpoint(
        path="/MailCampaignEmail/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MailCampaignEmail/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MailCampaignEmail",
        method="GET",
    )


class Mailcampaignlog:
    GET = Endpoint(
        path="/MailCampaignLog/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MailCampaignLog",
        method="GET",
    )


class Mailbox:
    CREATE = Endpoint(
        path="/Mailbox",
        method="POST",
        request_model="Mailbox",
    )
    DELETE = Endpoint(
        path="/Mailbox/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Mailbox/{id}",
        method="GET",
        summary="Get one Mailbox",
        description="Use this to return a single instance of Mailbox. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "includeglobalsmtp"],
    )
    GET_GET = Endpoint(
        path="/Mailbox/{id}/OutlookContacts",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Mailbox",
        method="GET",
        summary="List of Mailbox",
        description="Use this to return multiple Mailbox. Requires authentication.",
        query_params=["department_id", "from_addresses", "ignore_default", "organisation_id", "showall", "team_id"],
    )


class Mailboxcredential:
    CREATE = Endpoint(
        path="/MailboxCredential",
        method="POST",
        request_model="MailboxCredential",
    )
    DELETE = Endpoint(
        path="/MailboxCredential/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MailboxCredential/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MailboxCredential",
        method="GET",
    )


class Mailchimp:
    LIST = Endpoint(
        path="/Mailchimp/Get",
        method="GET",
    )


class Manageengine:
    LIST = Endpoint(
        path="/ManageEngine/Get",
        method="GET",
    )


class Manageenginedetails:
    CREATE = Endpoint(
        path="/ManageEngineDetails",
        method="POST",
        request_model="ManageEngineDetails",
    )
    DELETE = Endpoint(
        path="/ManageEngineDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ManageEngineDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ManageEngineDetails",
        method="GET",
    )


class Marketingunsubscribe:
    CREATE = Endpoint(
        path="/MarketingUnsubscribe",
        method="POST",
        request_model="MarketingUnsubscribe",
    )
    DELETE = Endpoint(
        path="/MarketingUnsubscribe/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MarketingUnsubscribe/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MarketingUnsubscribe",
        method="GET",
    )


class Mattermostchanneldetails:
    LIST = Endpoint(
        path="/MattermostChannelDetails",
        method="GET",
    )


class Mattermostdetails:
    CREATE = Endpoint(
        path="/MattermostDetails",
        method="POST",
        request_model="MattermostDetails",
    )
    DELETE = Endpoint(
        path="/MattermostDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MattermostDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MattermostDetails",
        method="GET",
    )


class Meterreading:
    CREATE = Endpoint(
        path="/MeterReading",
        method="POST",
        request_model="DeviceMeterReading",
    )
    GET = Endpoint(
        path="/MeterReading/{id}",
        method="GET",
        summary="Get one DeviceMeterReading",
        description="Use this to return a single instance of DeviceMeterReading. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/MeterReading",
        method="GET",
        summary="List of DeviceMeterReading",
        description="Use this to return multiple DeviceMeterReading. Requires authentication.",
        query_params=["asset_id", "count", "page_no", "page_size", "pageinate", "recurringinvoice_line_id"],
    )


class Microsoftsubscriptionmapping:
    CREATE = Endpoint(
        path="/MicrosoftSubscriptionMapping",
        method="POST",
        request_model="MicrosoftSubscriptionMapping",
    )
    DELETE = Endpoint(
        path="/MicrosoftSubscriptionMapping/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MicrosoftSubscriptionMapping/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MicrosoftSubscriptionMapping",
        method="GET",
    )


class Microsoftteams:
    LIST = Endpoint(
        path="/MicrosoftTeams/Get",
        method="GET",
    )


class Microsoftteamsmapping:
    CREATE = Endpoint(
        path="/MicrosoftTeamsMapping",
        method="POST",
        request_model="MicrosoftTeamsMapping",
    )
    DELETE = Endpoint(
        path="/MicrosoftTeamsMapping/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/MicrosoftTeamsMapping/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/MicrosoftTeamsMapping",
        method="GET",
    )


class Ncentraldetails:
    CREATE = Endpoint(
        path="/NCentralDetails",
        method="POST",
        request_model="NCentralDetails",
    )
    DELETE = Endpoint(
        path="/NCentralDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/NCentralDetails/{id}",
        method="GET",
        summary="Get one NCentralDetails",
        description="Use this to return a single instance of NCentralDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/NCentralDetails",
        method="GET",
        summary="List of NCentralDetails",
        description="Use this to return multiple NCentralDetails. Requires authentication.",
        query_params=["includedetails"],
    )


class Nhserverconfig:
    CREATE = Endpoint(
        path="/Nhserverconfig",
        method="POST",
        request_model="NHServerConfig",
    )
    DELETE = Endpoint(
        path="/Nhserverconfig/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Nhserverconfig/{id}",
        method="GET",
        summary="Get one NHServerConfig",
        description="Use this to return a single instance of NHServerConfig. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Nhserverconfig",
        method="GET",
    )


class Notification:
    CREATE = Endpoint(
        path="/Notification",
        method="POST",
        request_model="UnameNotification",
    )
    DELETE = Endpoint(
        path="/Notification/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Notification/{id}",
        method="GET",
        summary="Get one UnameNotification",
        description="Use this to return a single instance of UnameNotification. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Notification",
        method="GET",
        summary="List of UnameNotification",
        description="Use this to return multiple UnameNotification. Requires authentication.",
        query_params=["agent_id", "restrictto_agent_id", "role_id", "showall", "type", "webhook_id"],
    )


class Notificationlog:
    LIST = Endpoint(
        path="/NotificationLog",
        method="GET",
    )


class Notificationmessage:
    CREATE = Endpoint(
        path="/NotificationMessage",
        method="POST",
        request_model="NotificationContent",
    )
    DELETE = Endpoint(
        path="/NotificationMessage/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/NotificationMessage/{id}",
        method="GET",
        summary="Get one NotificationContent",
        description="Use this to return a single instance of NotificationContent. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/NotificationMessage",
        method="GET",
    )


class Notifications:
    CREATE = Endpoint(
        path="/Notifications",
        method="POST",
        request_model="EscMsg",
    )
    CREATE_POST = Endpoint(
        path="/Notifications/process",
        method="POST",
    )
    DELETE = Endpoint(
        path="/Notifications/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Notifications/{id}",
        method="GET",
        summary="Get one EscMsg",
        description="Use this to return a single instance of EscMsg. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Notifications",
        method="GET",
        summary="List of EscMsg",
        description="Use this to return multiple EscMsg. Requires authentication.",
        query_params=["checkhalointegrator", "checknhserver", "clientversion", "count", "newer_than_id", "older_than_id", "page_no", "page_size", "pageinate", "update_shown", "utc_offset"],
    )


class Objectmappingprofile:
    LIST = Endpoint(
        path="/ObjectMappingProfile",
        method="GET",
    )


class Onlinestatus:
    CREATE = Endpoint(
        path="/OnlineStatus",
        method="POST",
        request_model="OnlineStatus",
    )
    LIST = Endpoint(
        path="/OnlineStatus",
        method="GET",
        query_params=["TechID", "LastOnlineDate", "IsOnline", "LastOnline", "agent_status", "status_overidden", "fetch_all", "is_logout", "command", "last_active", "is_idle", "idle_warn"],
    )


class Opportunities:
    CREATE = Endpoint(
        path="/Opportunities",
        method="POST",
        request_model="Faults",
        response_model="Faults",
    )
    CREATE_POST = Endpoint(
        path="/Opportunities/View",
        method="POST",
        request_model="Faults",
    )
    DELETE = Endpoint(
        path="/Opportunities/{id}",
        method="DELETE",
        summary="Delete one Faults",
        description="Delete specific Faults. Requires authentication.",
        path_params=["id"],
        query_params=["reason"],
    )
    GET = Endpoint(
        path="/Opportunities/{id}",
        method="GET",
        summary="Get one Faults",
        description="Use this to return a single instance of Faults. Requires authentication.",
        path_params=["id"],
        query_params=["amailentryid", "assignedto", "consignablelines", "debug", "dodatabaselookup", "email", "include_auditing", "includeagent", "includechildids", "includedetails", "includelastaction", "includelastappointment", "includelinkedobjects", "includenextappointment", "includeparentchangeinfo", "includeparentsubject", "includeseenby", "is_portal", "isdetailscreen", "ishalolink", "ispreview", "isteams", "nocache", "subject", "ticketidonly", "utcoffset"],
        response_model="Faults",
    )
    LIST = Endpoint(
        path="/Opportunities",
        method="GET",
        summary="List of Faults",
        description="Use this to return multiple Faults. Requires authentication.",
        query_params=["advanced_search", "agent", "agent_id", "alerttype", "asset_id", "awaitinginput", "billableonly", "billing_date", "billing_type", "billingcontractid", "calendar_enddate", "calendar_startdate", "category_1", "category_2", "category_3", "category_4", "cf_display_values_only", "checkmyticketsonly", "client_id", "client_ids", "client_ref", "closed_only", "columns_id", "contract_id", "contract_period", "count", "datesearch", "debug", "default_columns", "deleted", "domain", "enddate", "enddatetime", "excludeslacalcs", "excludethese", "excludetickettypeallowall", "extraportalfilter", "facebook_id", "fetchgrandchildren", "flagged", "followedandagents", "ignoremilestonerestriction", "includeaccountmanager", "includeagent", "includeallopen", "includeappointmentid", "includeapproval", "includeassetkeyfield", "includeassettype", "includebreached", "includebudgettype", "includechildids", "includechildread", "includechildren", "includeclosed", "includecolumns", "includecompleted", "includecontract", "includecountryregion", "includefirstname", "include_custom_fields", "includefollowedonly", "includehold", "includeinactivetechs", "includeinactiveusers", "includeitilname", "includelastaction", "includelastincomingemail", "includelastname", "includelastnote", "includelocked", "includemailbox", "includemailid", "includemyuseronly", "includenextactivitydate", "includenextappointmenttype", "includeparentsubject", "includeprojects", "includeread", "includerelatedservices", "includerelease1", "includerelease2", "includerelease3", "includeservicecategory", "includeslaactiondate", "includeslatimer", "includestatus", "includesubmittedonly", "includesupplier", "includetickettype", "includetimetaken", "includetoplevel", "includeviewing", "includeworkflowstage", "includeworkflowstagenumber", "includuserdepartments", "inlcludeopenchildcount", "invlucebranch", "ismilestone", "isorion", "isquicktimesearch", "isscom", "isteams", "iszapier", "itil_requesttype", "itil_requesttype_id", "kanbanviewontheagentapp", "kanbanviewontheportal", "lastupdatefromdate", "lastupdatetodate", "list_id", "milestone_id", "mine", "nochargeonly", "notime", "onlytime", "open_only", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "orion_type", "page_no", "page_size", "pageinate", "parent_id", "pending_review", "per_action", "prepayorcontractonly", "priority", "product", "project_ids", "ready_for_invoicing", "related_id", "release_id", "requesttype", "requesttype_id", "requesttypegroup", "search", "search_details", "search_id", "search_inventory_number", "search_oppcompanyname", "search_oppcontactname", "search_oppemailaddress", "search_release1", "search_release2", "search_release3", "search_releasenote", "search_reportedby", "search_summary", "search_supplier_reference", "search_user_name", "search_version", "searchactions", "searchthisticketid", "service_id", "showonroadmap", "third_party_id", "third_party_id_string", "site_id", "sitepostcode", "sla", "sprint_for_tickettype_id", "sprints", "startandendset", "startdate", "startdatetime", "status", "status_id", "submittedandagents", "supplier_id", "supplier_status", "team", "team_name", "ticketarea_id", "ticketcontract_id", "ticketidonly", "ticketids", "ticketlinktype", "toplevel_id", "unlinked_only", "user_id", "username", "utcoffset", "view_id", "withattachments", "filetype_filter"],
        response_model="Faults_View",
    )


class Orderline:
    LIST = Endpoint(
        path="/OrderLine",
        method="GET",
    )


class Organisation:
    CREATE = Endpoint(
        path="/Organisation",
        method="POST",
        request_model="Organisation",
    )
    DELETE = Endpoint(
        path="/Organisation/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Organisation/{id}",
        method="GET",
        summary="Get one Organisation",
        description="Use this to return a single instance of Organisation. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Organisation",
        method="GET",
    )


class Outcome:
    CREATE = Endpoint(
        path="/Outcome",
        method="POST",
        request_model="TOutcome",
    )
    DELETE = Endpoint(
        path="/Outcome/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Outcome/{id}",
        method="GET",
        summary="Get one TOutcome",
        description="Use this to return a single instance of TOutcome. Requires authentication.",
        path_params=["id"],
        query_params=["action_id", "anon_ticketid", "contract_id", "debug", "includedetails", "invoice_id", "matched_kb_client_id", "matched_kbid", "override_user_id", "purchaseorder_id", "quotation_id", "salesorder_id", "selected_supplier_id", "ticket_id", "token"],
    )
    LIST = Endpoint(
        path="/Outcome",
        method="GET",
        summary="List of TOutcome",
        description="Use this to return multiple TOutcome. Requires authentication.",
        query_params=["access_control_level", "debug", "excludesystemactions", "quick_only", "showhidden", "showsystemactions", "slastate", "status", "supplier_id", "supplier_status", "tickettype_id", "workflow_id", "workflow_step"],
    )


class Outgoing:
    CREATE = Endpoint(
        path="/Outgoing",
        method="POST",
    )
    DELETE = Endpoint(
        path="/Outgoing/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Outgoing/{id}",
        method="GET",
        summary="Get one Outgoing",
        description="Use this to return a single instance of Outgoing. Requires authentication.",
        path_params=["id"],
        query_params=["includeattachments", "includedetails"],
    )
    LIST = Endpoint(
        path="/Outgoing",
        method="GET",
        summary="List of Outgoing",
        description="Use this to return multiple Outgoing. Requires authentication.",
        query_params=["count", "idonly", "mailbox_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "status_id"],
    )


class Outgoingattempt:
    GET = Endpoint(
        path="/OutgoingAttempt/{id}",
        method="GET",
        summary="Get one OutgoingAttempt",
        description="Use this to return a single instance of OutgoingAttempt. Requires authentication.",
        path_params=["id"],
        query_params=["includeattachments", "includedetails"],
    )
    LIST = Endpoint(
        path="/OutgoingAttempt",
        method="GET",
        summary="List of OutgoingAttempt",
        description="Use this to return multiple OutgoingAttempt. Requires authentication.",
        query_params=["count", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "outgoing_id", "page_no", "page_size", "pageinate"],
    )


class Outgoingemail:
    CREATE = Endpoint(
        path="/Outgoingemail",
        method="POST",
        request_model="Outgoingemail",
    )
    DELETE = Endpoint(
        path="/Outgoingemail/{id}",
        method="DELETE",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Outgoingemail",
        method="GET",
        summary="List of Outgoingemail",
        description="Use this to return multiple Outgoingemail. Requires authentication.",
        query_params=["errorsonly"],
    )


class Prtgdetails:
    CREATE = Endpoint(
        path="/PRTGDetails",
        method="POST",
        request_model="PRTGDetails",
    )
    DELETE = Endpoint(
        path="/PRTGDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/PRTGDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/PRTGDetails",
        method="GET",
    )


class Passwordfield:
    CREATE = Endpoint(
        path="/PasswordField",
        method="POST",
        request_model="AuditPasswordField",
    )
    GET = Endpoint(
        path="/PasswordField/{id}",
        method="GET",
        summary="Get one AuditPasswordField",
        description="Use this to return a single instance of AuditPasswordField. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/PasswordField",
        method="GET",
    )


class Pax8Details:
    CREATE = Endpoint(
        path="/Pax8Details",
        method="POST",
        request_model="Pax8Details",
    )
    DELETE = Endpoint(
        path="/Pax8Details/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Pax8Details/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/Pax8Details",
        method="GET",
    )


class Pdftemplate:
    CREATE = Endpoint(
        path="/PdfTemplate",
        method="POST",
        request_model="PdfTemplate",
    )
    DELETE = Endpoint(
        path="/PdfTemplate/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/PdfTemplate/{id}",
        method="GET",
        summary="Get one PdfTemplate",
        description="Use this to return a single instance of PdfTemplate. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "licencename", "system_use"],
    )
    LIST = Endpoint(
        path="/PdfTemplate",
        method="GET",
        summary="List of PdfTemplate",
        description="Use this to return multiple PdfTemplate. Requires authentication.",
        query_params=["licencename", "type"],
    )


class Pdftemplaterepository:
    GET = Endpoint(
        path="/PdfTemplateRepository/{id}",
        method="GET",
        summary="Get one PdfTemplate",
        description="Use this to return a single instance of PdfTemplate. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "licencename", "system_use"],
    )
    LIST = Endpoint(
        path="/PdfTemplateRepository",
        method="GET",
        summary="List of PdfTemplate",
        description="Use this to return multiple PdfTemplate. Requires authentication.",
        query_params=["licencename", "type"],
    )


class Popupnote:
    CREATE = Endpoint(
        path="/PopupNote/read",
        method="POST",
        request_model="AreaPopup",
    )
    LIST = Endpoint(
        path="/PopupNote",
        method="GET",
        summary="List of AreaPopup",
        description="Use this to return multiple AreaPopup. Requires authentication.",
        query_params=["client_id", "showall", "site_id", "user_id"],
    )


class Powershellscript:
    CREATE = Endpoint(
        path="/PowerShellScript",
        method="POST",
        request_model="PowerShellScript",
    )
    DELETE = Endpoint(
        path="/PowerShellScript/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/PowerShellScript/{id}",
        method="GET",
        summary="Get one PowerShellScript",
        description="Use this to return a single instance of PowerShellScript. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/PowerShellScript",
        method="GET",
        summary="List of PowerShellScript",
        description="Use this to return multiple PowerShellScript. Requires authentication.",
        query_params=["clientidoverride", "type"],
    )


class Powershellscriptcriteria:
    CREATE = Endpoint(
        path="/PowerShellScriptCriteria",
        method="POST",
        request_model="PowerShellScriptCriteria",
    )
    DELETE = Endpoint(
        path="/PowerShellScriptCriteria/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/PowerShellScriptCriteria/{id}",
        method="GET",
        summary="Get one PowerShellScriptCriteria",
        description="Use this to return a single instance of PowerShellScriptCriteria. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/PowerShellScriptCriteria",
        method="GET",
        summary="List of PowerShellScriptCriteria",
        description="Use this to return multiple PowerShellScriptCriteria. Requires authentication.",
        query_params=["script_id"],
    )


class Powershellscriptprocessing:
    CREATE = Endpoint(
        path="/PowerShellScriptProcessing",
        method="POST",
        request_model="PowerShellScriptProcessing",
    )
    DELETE = Endpoint(
        path="/PowerShellScriptProcessing/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/PowerShellScriptProcessing/{id}",
        method="GET",
        summary="Get one PowerShellScriptProcessing",
        description="Use this to return a single instance of PowerShellScriptProcessing. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/PowerShellScriptProcessing",
        method="GET",
        summary="List of PowerShellScriptProcessing",
        description="Use this to return multiple PowerShellScriptProcessing. Requires authentication.",
        query_params=["count", "includeparameters", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "outstandingonly", "page_no", "page_size", "pageinate", "script_id", "ticket_id"],
    )


class Priority:
    CREATE = Endpoint(
        path="/Priority",
        method="POST",
        request_model="Policy",
    )
    DELETE = Endpoint(
        path="/Priority/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Priority/{id}",
        method="GET",
        summary="Get one Policy",
        description="Use this to return a single instance of Policy. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Priority",
        method="GET",
        summary="List of Policy",
        description="Use this to return multiple Policy. Requires authentication.",
        query_params=["includedistinct", "slaid"],
    )


class Product:
    CREATE = Endpoint(
        path="/Product",
        method="POST",
        request_model="ReleaseProduct",
    )
    DELETE = Endpoint(
        path="/Product/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Product/{id}",
        method="GET",
        summary="Get one ReleaseProduct",
        description="Use this to return a single instance of ReleaseProduct. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Product",
        method="GET",
        summary="List of ReleaseProduct",
        description="Use this to return multiple ReleaseProduct. Requires authentication.",
        query_params=["devops_instance", "third_party_only"],
    )


class Productbranch:
    LIST = Endpoint(
        path="/ProductBranch",
        method="GET",
        summary="List of ReleaseBranch",
        description="Use this to return multiple ReleaseBranch. Requires authentication.",
        query_params=["product_id"],
    )


class Productcomponent:
    CREATE = Endpoint(
        path="/ProductComponent",
        method="POST",
        request_model="ReleaseComponent",
    )
    DELETE = Endpoint(
        path="/ProductComponent/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ProductComponent/{id}",
        method="GET",
        summary="Get one ReleaseComponent",
        description="Use this to return a single instance of ReleaseComponent. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ProductComponent",
        method="GET",
        summary="List of ReleaseComponent",
        description="Use this to return multiple ReleaseComponent. Requires authentication.",
        query_params=["product_id"],
    )


class Projectsetuplines:
    CREATE = Endpoint(
        path="/ProjectSetupLines",
        method="POST",
        request_model="ProjectSetupLines",
    )


class Projects:
    CREATE = Endpoint(
        path="/Projects",
        method="POST",
        request_model="Faults",
        response_model="Faults",
    )
    CREATE_POST = Endpoint(
        path="/Projects/View",
        method="POST",
        request_model="Faults",
    )
    DELETE = Endpoint(
        path="/Projects/{id}",
        method="DELETE",
        summary="Delete one Faults",
        description="Delete specific Faults. Requires authentication.",
        path_params=["id"],
        query_params=["reason"],
    )
    GET = Endpoint(
        path="/Projects/{id}",
        method="GET",
        summary="Get one Faults",
        description="Use this to return a single instance of Faults. Requires authentication.",
        path_params=["id"],
        query_params=["amailentryid", "assignedto", "consignablelines", "debug", "dodatabaselookup", "email", "include_auditing", "includeagent", "includechildids", "includedetails", "includelastaction", "includelastappointment", "includelinkedobjects", "includenextappointment", "includeparentchangeinfo", "includeparentsubject", "includeseenby", "is_portal", "isdetailscreen", "ishalolink", "ispreview", "isteams", "nocache", "subject", "ticketidonly", "utcoffset"],
        response_model="Faults",
    )
    LIST = Endpoint(
        path="/Projects",
        method="GET",
        summary="List of Faults",
        description="Use this to return multiple Faults. Requires authentication.",
        query_params=["advanced_search", "agent", "agent_id", "alerttype", "asset_id", "awaitinginput", "billableonly", "billing_date", "billing_type", "billingcontractid", "calendar_enddate", "calendar_startdate", "category_1", "category_2", "category_3", "category_4", "cf_display_values_only", "checkmyticketsonly", "client_id", "client_ids", "client_ref", "closed_only", "columns_id", "contract_id", "contract_period", "count", "datesearch", "debug", "default_columns", "deleted", "domain", "enddate", "enddatetime", "excludeslacalcs", "excludethese", "excludetickettypeallowall", "extraportalfilter", "facebook_id", "fetchgrandchildren", "flagged", "followedandagents", "ignoremilestonerestriction", "includeaccountmanager", "includeagent", "includeallopen", "includeappointmentid", "includeapproval", "includeassetkeyfield", "includeassettype", "includebreached", "includebudgettype", "includechildids", "includechildread", "includechildren", "includeclosed", "includecolumns", "includecompleted", "includecontract", "includecountryregion", "includefirstname", "include_custom_fields", "includefollowedonly", "includehold", "includeinactivetechs", "includeinactiveusers", "includeitilname", "includelastaction", "includelastincomingemail", "includelastname", "includelastnote", "includelocked", "includemailbox", "includemailid", "includemyuseronly", "includenextactivitydate", "includenextappointmenttype", "includeparentsubject", "includeprojects", "includeread", "includerelatedservices", "includerelease1", "includerelease2", "includerelease3", "includeservicecategory", "includeslaactiondate", "includeslatimer", "includestatus", "includesubmittedonly", "includesupplier", "includetickettype", "includetimetaken", "includetoplevel", "includeviewing", "includeworkflowstage", "includeworkflowstagenumber", "includuserdepartments", "inlcludeopenchildcount", "invlucebranch", "ismilestone", "isorion", "isquicktimesearch", "isscom", "isteams", "iszapier", "itil_requesttype", "itil_requesttype_id", "kanbanviewontheagentapp", "kanbanviewontheportal", "lastupdatefromdate", "lastupdatetodate", "list_id", "milestone_id", "mine", "nochargeonly", "notime", "onlytime", "open_only", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "orion_type", "page_no", "page_size", "pageinate", "parent_id", "pending_review", "per_action", "prepayorcontractonly", "priority", "product", "project_ids", "ready_for_invoicing", "related_id", "release_id", "requesttype", "requesttype_id", "requesttypegroup", "search", "search_details", "search_id", "search_inventory_number", "search_oppcompanyname", "search_oppcontactname", "search_oppemailaddress", "search_release1", "search_release2", "search_release3", "search_releasenote", "search_reportedby", "search_summary", "search_supplier_reference", "search_user_name", "search_version", "searchactions", "searchthisticketid", "service_id", "showonroadmap", "third_party_id", "third_party_id_string", "site_id", "sitepostcode", "sla", "sprint_for_tickettype_id", "sprints", "startandendset", "startdate", "startdatetime", "status", "status_id", "submittedandagents", "supplier_id", "supplier_status", "team", "team_name", "ticketarea_id", "ticketcontract_id", "ticketidonly", "ticketids", "ticketlinktype", "toplevel_id", "unlinked_only", "user_id", "username", "utcoffset", "view_id", "withattachments", "filetype_filter"],
        response_model="Faults_View",
    )


class Publishprofiles:
    CREATE = Endpoint(
        path="/PublishProfiles",
        method="POST",
        request_model="PublishProfiles",
    )
    DELETE = Endpoint(
        path="/PublishProfiles/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/PublishProfiles/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/PublishProfiles",
        method="GET",
    )


class Purchaseorder:
    CREATE = Endpoint(
        path="/PurchaseOrder",
        method="POST",
        request_model="SupplierOrderHeader",
        response_model="SupplierOrderHeader",
    )
    CREATE_POST = Endpoint(
        path="/PurchaseOrder/View",
        method="POST",
        request_model="Viewers",
    )
    DELETE = Endpoint(
        path="/PurchaseOrder/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/PurchaseOrder/{id}",
        method="GET",
        summary="Get one SupplierOrderHeader",
        description="Use this to return a single instance of SupplierOrderHeader. Requires authentication.",
        path_params=["id"],
        query_params=["extrareceivablelines", "includedetails", "invoiceablelines", "receivablelines"],
        response_model="SupplierOrderHeader",
    )
    LIST = Endpoint(
        path="/PurchaseOrder",
        method="GET",
        summary="List of SupplierOrderHeader",
        description="Use this to return multiple SupplierOrderHeader. Requires authentication.",
        query_params=["awaiting_approval", "awaitingstock", "client_id", "closed", "count", "deliver_to_us", "deliver_to_user_salesorder_id", "my_approvals", "open", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "po_status", "salesorder_id", "search", "site_id", "supplier_id", "ticket_id", "unsent", "user_id"],
        response_model="SupplierOrderHeader_View",
    )


class Qualification:
    CREATE = Endpoint(
        path="/Qualification",
        method="POST",
        request_model="Qualification",
    )
    DELETE = Endpoint(
        path="/Qualification/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Qualification/{id}",
        method="GET",
        summary="Get one Qualification",
        description="Use this to return a single instance of Qualification. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Qualification",
        method="GET",
        summary="List of Qualification",
        description="Use this to return multiple Qualification. Requires authentication.",
        query_params=["includecriteriainfo"],
    )


class Quickbooksdetails:
    CREATE = Endpoint(
        path="/QuickBooksDetails",
        method="POST",
        request_model="QuickBooksDetails",
    )
    DELETE = Endpoint(
        path="/QuickBooksDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/QuickBooksDetails/{id}",
        method="GET",
        summary="Get one QuickBooksDetails",
        description="Use this to return a single instance of QuickBooksDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/QuickBooksDetails",
        method="GET",
        summary="List of QuickBooksDetails",
        description="Use this to return multiple QuickBooksDetails. Requires authentication.",
        query_params=["companyid", "connectedonly"],
    )


class Quotation:
    CREATE = Endpoint(
        path="/Quotation",
        method="POST",
        request_model="QuotationHeader",
        response_model="QuotationHeader",
    )
    CREATE_POST = Endpoint(
        path="/Quotation/Lines",
        method="POST",
        request_model="QuotationDetail",
    )
    DELETE = Endpoint(
        path="/Quotation/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Quotation/{id}",
        method="GET",
        summary="Get one QuotationHeader",
        description="Use this to return a single instance of QuotationHeader. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "isportalview"],
        response_model="QuotationHeader",
    )
    LIST = Endpoint(
        path="/Quotation",
        method="GET",
        summary="List of QuotationHeader",
        description="Use this to return multiple QuotationHeader. Requires authentication.",
        query_params=["awaiting_approval", "client_id", "closed", "count", "currentclientorall", "includelines", "my_approvals", "needsprocessing", "open", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "processed", "quote_status", "search", "site_id", "ticket_id", "user_id", "filetype_filter"],
        response_model="QuotationHeader_View",
    )


class Raynet:
    LIST = Endpoint(
        path="/Raynet/Get",
        method="GET",
    )


class Raynetdetails:
    CREATE = Endpoint(
        path="/RaynetDetails",
        method="POST",
        request_model="RaynetDetails",
    )
    DELETE = Endpoint(
        path="/RaynetDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/RaynetDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/RaynetDetails",
        method="GET",
    )


class Recurringinvoice:
    CREATE = Endpoint(
        path="/RecurringInvoice",
        method="POST",
        request_model="InvoiceHeader",
        response_model="InvoiceHeader",
    )
    CREATE_POST = Endpoint(
        path="/RecurringInvoice/Lines",
        method="POST",
        request_model="InvoiceDetail",
    )
    DELETE = Endpoint(
        path="/RecurringInvoice/{id}",
        method="DELETE",
        summary="Delete one InvoiceHeader",
        description="Delete specific InvoiceHeader. Requires authentication.",
        path_params=["id"],
        query_params=["bypass_accounts_sync"],
    )
    GET = Endpoint(
        path="/RecurringInvoice/{id}",
        method="GET",
        summary="Get one InvoiceHeader",
        description="Use this to return a single instance of InvoiceHeader. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
        response_model="InvoiceHeader",
    )
    LIST = Endpoint(
        path="/RecurringInvoice",
        method="GET",
        summary="List of InvoiceHeader",
        description="Use this to return multiple InvoiceHeader. Requires authentication.",
        query_params=["advanced_search", "asset_id", "awaiting_approval", "billing_date", "billingcategory_ids", "start_date", "end_date", "datesearch", "client_id", "client_ids", "contract_id", "count", "idonly", "includecredits", "includeinvoices", "includelines", "includepoinvoices", "invoicedateend", "invoicedatestart", "my_approvals", "notpostedonly", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "paymentstatuses", "postedonly", "purchaseorder_id", "quote_status", "ready_for_invoicing", "recurringinvoice_id", "reviewrequired", "rinvoice_type", "salesorder_id", "search", "sent_status", "site_id", "stripeautopaymentrequired", "ticket_id", "toplevel_id", "user_id", "third_party_id", "xero_id", "quickbooks_id", "include_linked_item_details"],
        response_model="InvoiceHeader_View",
    )


class Recurringitem:
    LIST = Endpoint(
        path="/RecurringItem",
        method="GET",
        summary="List of AreaItem",
        description="Use this to return multiple AreaItem. Requires authentication.",
        query_params=["client_id", "pending_recurring_invoice"],
    )


class Release:
    CREATE = Endpoint(
        path="/Release",
        method="POST",
        request_model="Release",
    )
    DELETE = Endpoint(
        path="/Release/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Release/{id}",
        method="GET",
        summary="Get one Release",
        description="Use this to return a single instance of Release. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Release",
        method="GET",
        description=". Requires authentication.",
        query_params=["count", "include_devops_project", "includenotecount", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "product_id", "restrictmyversion", "search", "compare_version_seq", "exclude_releasenote_group_id", "includedetails", "releasenote_group_id"],
    )


class Releasenotegroup:
    CREATE = Endpoint(
        path="/ReleaseNoteGroup",
        method="POST",
        request_model="ReleaseNoteGroup",
    )
    DELETE = Endpoint(
        path="/ReleaseNoteGroup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ReleaseNoteGroup/{id}",
        method="GET",
        summary="Get one ReleaseNoteGroup",
        description="Use this to return a single instance of ReleaseNoteGroup. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ReleaseNoteGroup",
        method="GET",
    )


class Releasepipeline:
    CREATE = Endpoint(
        path="/ReleasePipeline",
        method="POST",
        request_model="ReleasePipeline",
    )
    DELETE = Endpoint(
        path="/ReleasePipeline/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ReleasePipeline/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ReleasePipeline",
        method="GET",
    )


class Releasetype:
    CREATE = Endpoint(
        path="/ReleaseType",
        method="POST",
        request_model="ReleaseType",
    )
    DELETE = Endpoint(
        path="/ReleaseType/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ReleaseType/{id}",
        method="GET",
        summary="Get one ReleaseType",
        description="Use this to return a single instance of ReleaseType. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ReleaseType",
        method="GET",
    )


class Remotesession:
    CREATE = Endpoint(
        path="/RemoteSession",
        method="POST",
        request_model="RemoteSessionData",
    )
    DELETE = Endpoint(
        path="/RemoteSession/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/RemoteSession/{id}",
        method="GET",
        summary="Get one RemoteSessionData",
        description="Use this to return a single instance of RemoteSessionData. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/RemoteSession",
        method="GET",
        summary="List of RemoteSessionData",
        description="Use this to return multiple RemoteSessionData. Requires authentication.",
        query_params=["agent", "agent_id", "client_id", "count", "includelinked", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "site_id", "username"],
    )


class Remotesessionteams:
    LIST = Endpoint(
        path="/RemoteSessionTeams",
        method="GET",
        summary="List of RemoteSessionTeams",
        description="Use this to return multiple RemoteSessionTeams. Requires authentication.",
        query_params=["includeenabled", "msid"],
    )


class Report:
    CREATE = Endpoint(
        path="/Report",
        method="POST",
        request_model="AnalyzerProfile",
        response_model="AnalyzerProfile",
    )
    CREATE_POST = Endpoint(
        path="/Report/Bookmark",
        method="POST",
        request_model="AnalyzerProfile",
    )
    DELETE = Endpoint(
        path="/Report/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Report/{id}",
        method="GET",
        summary="Get one AnalyzerProfile",
        description="Use this to return a single instance of AnalyzerProfile. Requires authentication.",
        path_params=["id"],
        query_params=["client_id", "clientname", "dashboard_id", "dashboard_published_id", "dontloadsystemreport", "getcompositetoken", "includedetails", "invoice_id", "loadreport", "report_access_token", "reportingperiod", "reportingperiodenddate", "reportingperiodstartdate"],
        response_model="AnalyzerProfile",
    )
    LIST = Endpoint(
        path="/Report",
        method="GET",
        summary="List of AnalyzerProfile",
        description="Use this to return multiple AnalyzerProfile. Requires authentication.",
        query_params=["agentrestriction", "chartonly", "clientname", "count", "includepublished", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "reportgroup_id", "search", "type"],
        response_model="AnalyzerProfile_View",
    )


class Reportdata:
    GET = Endpoint(
        path="/ReportData/{publishedid}",
        method="GET",
        path_params=["publishedid"],
    )


class Reportrepository:
    GET = Endpoint(
        path="/ReportRepository/{id}",
        method="GET",
        summary="Get one AnalyzerProfile",
        description="Use this to return a single instance of AnalyzerProfile. Requires authentication.",
        path_params=["id"],
        query_params=["client_id", "clientname", "dashboard_id", "dashboard_published_id", "dontloadsystemreport", "getcompositetoken", "includedetails", "invoice_id", "loadreport", "report_access_token", "reportingperiod", "reportingperiodenddate", "reportingperiodstartdate"],
    )
    LIST = Endpoint(
        path="/ReportRepository",
        method="GET",
        summary="List of AnalyzerProfile",
        description="Use this to return multiple AnalyzerProfile. Requires authentication.",
        query_params=["agentrestriction", "chartonly", "clientname", "count", "includepublished", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "reportgroup_id", "search", "type"],
    )
    LIST_GET = Endpoint(
        path="/ReportRepository/ReportCategories",
        method="GET",
        summary="List of Lookup",
        description="Use this to return multiple Lookup. Requires authentication.",
        query_params=["access_control_level", "assettype_id", "client_id", "clientname", "contract_id", "country_code_id", "dbc_company_id", "domain", "exclude_nocharge", "exclude_nolinkedtypes", "exclude_zero", "iscustomfield", "istree", "lookupid", "ordervaluetype", "outcome_id", "showallcodes", "ticket_id", "unameaprestriction", "use", "use2"],
    )


class Resourcetype:
    GET = Endpoint(
        path="/ResourceType/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ResourceType",
        method="GET",
    )


class Roadmap:
    LIST = Endpoint(
        path="/Roadmap",
        method="GET",
        description=". Requires authentication.",
        query_params=["halocrm", "haloitsm", "halopsa", "haloservicedesk", "order", "orderdesc", "product_id", "roadmapcolumnview"],
    )


class Roles:
    CREATE = Endpoint(
        path="/Roles",
        method="POST",
        request_model="NHD_Roles",
    )
    DELETE = Endpoint(
        path="/Roles/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Roles/{id}",
        method="GET",
        summary="Get one NHD_Roles",
        description="Use this to return a single instance of NHD_Roles. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "isconfig"],
    )
    LIST = Endpoint(
        path="/Roles",
        method="GET",
        summary="List of NHD_Roles",
        description="Use this to return multiple NHD_Roles. Requires authentication.",
        query_params=["access_control_level", "agentid", "isconfig"],
    )


class Sla:
    CREATE = Endpoint(
        path="/SLA",
        method="POST",
        request_model="SlaHead",
    )
    DELETE = Endpoint(
        path="/SLA/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SLA/{id}",
        method="GET",
        summary="Get one SlaHead",
        description="Use this to return a single instance of SlaHead. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/SLA",
        method="GET",
        summary="List of SlaHead",
        description="Use this to return multiple SlaHead. Requires authentication.",
        query_params=["access_control_level", "isconfig", "showpriorities", "showworkdays"],
    )


class Sqlimport:
    CREATE = Endpoint(
        path="/SQLImport",
        method="POST",
        request_model="SQLImport",
    )
    DELETE = Endpoint(
        path="/SQLImport/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SQLImport/{id}",
        method="GET",
        summary="Get one SQLImport",
        description="Use this to return a single instance of SQLImport. Requires authentication.",
        path_params=["id"],
        query_params=["clientidoverride", "includedetails"],
    )
    LIST = Endpoint(
        path="/SQLImport",
        method="GET",
        summary="List of SQLImport",
        description="Use this to return multiple SQLImport. Requires authentication.",
        query_params=["clientidoverride", "integratorenabled", "showpositiveonly"],
    )


class Sagebusinessclouddetails:
    CREATE = Endpoint(
        path="/SageBusinessCloudDetails",
        method="POST",
        request_model="SageBusinessCloudDetails",
    )
    DELETE = Endpoint(
        path="/SageBusinessCloudDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SageBusinessCloudDetails/{id}",
        method="GET",
        summary="Get one SageBusinessCloudDetails",
        description="Use this to return a single instance of SageBusinessCloudDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/SageBusinessCloudDetails",
        method="GET",
        summary="List of SageBusinessCloudDetails",
        description="Use this to return multiple SageBusinessCloudDetails. Requires authentication.",
        query_params=["connectedonly", "tenantid"],
    )


class Sailpointdetails:
    CREATE = Endpoint(
        path="/SailPointDetails",
        method="POST",
        request_model="SailPointDetails",
    )
    DELETE = Endpoint(
        path="/SailPointDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SailPointDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SailPointDetails",
        method="GET",
    )


class Sailpointrolemapping:
    LIST = Endpoint(
        path="/SailPointRoleMapping",
        method="GET",
    )


class Sailpointusermapping:
    LIST = Endpoint(
        path="/SailPointUserMapping",
        method="GET",
    )


class Salesmailbox:
    CREATE = Endpoint(
        path="/SalesMailbox",
        method="POST",
        request_model="SalesMailbox",
    )
    DELETE = Endpoint(
        path="/SalesMailbox/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SalesMailbox/{id}",
        method="GET",
        summary="Get one SalesMailbox",
        description="Use this to return a single instance of SalesMailbox. Requires authentication.",
        path_params=["id"],
        query_params=["_test_access", "includedetails"],
    )
    LIST = Endpoint(
        path="/SalesMailbox",
        method="GET",
    )


class Salesmailboxdetail:
    CREATE = Endpoint(
        path="/SalesMailboxDetail",
        method="POST",
        request_model="SalesMailboxDetail",
    )
    LIST = Endpoint(
        path="/SalesMailboxDetail",
        method="GET",
    )


class Salesorder:
    CREATE = Endpoint(
        path="/SalesOrder",
        method="POST",
        request_model="OrderHead",
        response_model="OrderHead",
    )
    CREATE_POST = Endpoint(
        path="/SalesOrder/View",
        method="POST",
        request_model="Viewers",
    )
    DELETE = Endpoint(
        path="/SalesOrder/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SalesOrder/{id}",
        method="GET",
        summary="Get one OrderHead",
        description="Use this to return a single instance of OrderHead. Requires authentication.",
        path_params=["id"],
        query_params=["consignablelines", "includedetails", "invoiceablelines", "oneline", "pendingpolines"],
        response_model="OrderHead",
    )
    LIST = Endpoint(
        path="/SalesOrder",
        method="GET",
        summary="List of OrderHead",
        description="Use this to return multiple OrderHead. Requires authentication.",
        query_params=["advanced_search", "billing_date", "client_id", "client_ids", "closed", "count", "idonly", "needsconsigning", "needsinvoicing", "needsordering", "open", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "quote_status", "ready_for_invoicing", "search", "site_id", "ticket_id", "toplevel_id", "user_id"],
        response_model="OrderHead_View",
    )


class Savedforecast:
    CREATE = Endpoint(
        path="/SavedForecast",
        method="POST",
        request_model="SavedForecast",
    )
    DELETE = Endpoint(
        path="/SavedForecast/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SavedForecast/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SavedForecast",
        method="GET",
    )


class Schedule:
    CREATE = Endpoint(
        path="/Schedule",
        method="POST",
        request_model="Schedule",
    )
    GET = Endpoint(
        path="/Schedule/{id}",
        method="GET",
        summary="Get one Schedule",
        description="Use this to return a single instance of Schedule. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Schedule",
        method="GET",
        summary="List of Schedule",
        description="Use this to return multiple Schedule. Requires authentication.",
        query_params=["includedetails", "primaryid", "type"],
    )


class Scheduleoccurrence:
    CREATE = Endpoint(
        path="/ScheduleOccurrence",
        method="POST",
    )
    GET = Endpoint(
        path="/ScheduleOccurrence/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ScheduleOccurrence",
        method="GET",
    )


class Screenlayout:
    CREATE = Endpoint(
        path="/ScreenLayout",
        method="POST",
        request_model="ScreenLayout",
    )
    DELETE = Endpoint(
        path="/ScreenLayout/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ScreenLayout/{id}",
        method="GET",
        summary="Get one ScreenLayout",
        description="Use this to return a single instance of ScreenLayout. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ScreenLayout",
        method="GET",
        summary="List of ScreenLayout",
        description="Use this to return multiple ScreenLayout. Requires authentication.",
        query_params=["typeid"],
    )


class Search:
    LIST = Endpoint(
        path="/Search",
        method="GET",
        summary="List of Search",
        description="Use this to return multiple Search. Requires authentication.",
        query_params=["count_per_entity", "search"],
    )


class Securesecretlink:
    CREATE = Endpoint(
        path="/SecureSecretLink",
        method="POST",
        request_model="SecureSecretLink",
    )
    DELETE = Endpoint(
        path="/SecureSecretLink/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SecureSecretLink/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SecureSecretLink",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/SecureSecretLink/validate",
        method="GET",
        query_params=["token", "passphrase"],
    )


class Securitycheck:
    LIST = Endpoint(
        path="/SecurityCheck",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/SecurityCheck/oldencryption",
        method="GET",
    )


class Securityquestion:
    CREATE = Endpoint(
        path="/SecurityQuestion",
        method="POST",
        request_model="SecurityQuestion",
    )
    DELETE = Endpoint(
        path="/SecurityQuestion/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SecurityQuestion/{id}",
        method="GET",
        summary="Get one SecurityQuestion",
        description="Use this to return a single instance of SecurityQuestion. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/SecurityQuestion",
        method="GET",
    )


class Securityquestionvalidate:
    CREATE = Endpoint(
        path="/SecurityQuestionValidate",
        method="POST",
        request_model="NPR_Result",
    )
    LIST = Endpoint(
        path="/SecurityQuestionValidate",
        method="GET",
    )


class Sentinelone:
    LIST = Endpoint(
        path="/SentinelOne/Get",
        method="GET",
    )


class Sentinelonedetails:
    CREATE = Endpoint(
        path="/SentinelOneDetails",
        method="POST",
        request_model="SentinelOneDetails",
    )
    DELETE = Endpoint(
        path="/SentinelOneDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SentinelOneDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SentinelOneDetails",
        method="GET",
    )


class Service:
    CREATE = Endpoint(
        path="/Service",
        method="POST",
        request_model="ServSite",
        response_model="ServSite",
    )
    CREATE_POST = Endpoint(
        path="/Service/unsubscribe",
        method="POST",
        request_model="UnsubscribeService",
    )
    DELETE = Endpoint(
        path="/Service/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Service/{id}",
        method="GET",
        summary="Get one ServSite",
        description="Use this to return a single instance of ServSite. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "user_id"],
        response_model="ServSite",
    )
    LIST = Endpoint(
        path="/Service",
        method="GET",
        summary="List of ServSite",
        description="Use this to return multiple ServSite. Requires authentication.",
        query_params=["access_control_level", "asset_ids", "count", "includechildservices", "includestatusinfo", "itil_ticket_type", "monitoredonly", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "parent_service_category_id", "relatedservicesonly", "search", "service_category_id", "service_category_ids", "service_status_ids", "subscribedonly", "template_id", "ticket_id", "tickettype_id", "user_id"],
        response_model="ServSite_View",
    )


class Serviceavailability:
    CREATE = Endpoint(
        path="/ServiceAvailability",
        method="POST",
        request_model="ServiceAvailability",
    )
    DELETE = Endpoint(
        path="/ServiceAvailability/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ServiceAvailability/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ServiceAvailability",
        method="GET",
    )


class Servicecategory:
    CREATE = Endpoint(
        path="/ServiceCategory",
        method="POST",
        request_model="ServiceCategory",
    )
    DELETE = Endpoint(
        path="/ServiceCategory/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ServiceCategory/{id}",
        method="GET",
        summary="Get one ServiceCategory",
        description="Use this to return a single instance of ServiceCategory. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ServiceCategory",
        method="GET",
        summary="List of ServiceCategory",
        description="Use this to return multiple ServiceCategory. Requires authentication.",
        query_params=["access_control_level", "include_parent_name", "itil_ticket_type", "user_id"],
    )


class Servicerequestdetails:
    GET = Endpoint(
        path="/ServiceRequestDetails/{id}",
        method="GET",
        summary="Get one ServiceRequestDetails",
        description="Use this to return a single instance of ServiceRequestDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ServiceRequestDetails",
        method="GET",
        summary="List of ServiceRequestDetails",
        description="Use this to return multiple ServiceRequestDetails. Requires authentication.",
        query_params=["exclude_urls", "includedetails", "service_id"],
    )


class Servicerestriction:
    LIST = Endpoint(
        path="/ServiceRestriction",
        method="GET",
        summary="List of ServiceRestriction",
        description="Use this to return multiple ServiceRestriction. Requires authentication.",
        query_params=["client_id", "service_category_id", "service_id"],
    )


class Servicestatus:
    CREATE = Endpoint(
        path="/ServiceStatus",
        method="POST",
        request_model="ServStatus",
    )
    CREATE_POST = Endpoint(
        path="/ServiceStatus/Subscribe",
        method="POST",
        request_model="ServStatusSubscribe",
    )
    DELETE = Endpoint(
        path="/ServiceStatus/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ServiceStatus/Subscribe/{id}",
        method="GET",
        path_params=["id"],
    )
    GET_GET = Endpoint(
        path="/ServiceStatus/{id}",
        method="GET",
        summary="Get one ServStatus",
        description="Use this to return a single instance of ServStatus. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ServiceStatus",
        method="GET",
        summary="List of ServStatus",
        description="Use this to return multiple ServStatus. Requires authentication.",
        query_params=["count", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "service_id"],
    )


class Setuptab:
    CREATE = Endpoint(
        path="/SetupTab",
        method="POST",
        request_model="SetupTab",
    )
    GET = Endpoint(
        path="/SetupTab/{id}",
        method="GET",
        summary="Get one SetupTab",
        description="Use this to return a single instance of SetupTab. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/SetupTab",
        method="GET",
    )


class Setuptabgroup:
    GET = Endpoint(
        path="/SetupTabGroup/{id}",
        method="GET",
        summary="Get one SetupTabGroup",
        description="Use this to return a single instance of SetupTabGroup. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/SetupTabGroup",
        method="GET",
    )


class Sharepoint:
    LIST = Endpoint(
        path="/SharePoint/Get",
        method="GET",
    )


class Shopifydetails:
    CREATE = Endpoint(
        path="/ShopifyDetails",
        method="POST",
        request_model="ShopifyDetails",
    )
    DELETE = Endpoint(
        path="/ShopifyDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ShopifyDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ShopifyDetails",
        method="GET",
    )


class Singlesignonapplication:
    CREATE = Endpoint(
        path="/SingleSignOnApplication",
        method="POST",
        request_model="SingleSignOnApplication",
    )
    DELETE = Endpoint(
        path="/SingleSignOnApplication/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SingleSignOnApplication/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SingleSignOnApplication",
        method="GET",
    )


class Singlesignonattempt:
    DELETE = Endpoint(
        path="/SingleSignOnAttempt/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SingleSignOnAttempt/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SingleSignOnAttempt",
        method="GET",
    )


class Site:
    CREATE = Endpoint(
        path="/Site",
        method="POST",
        request_model="Site",
        response_model="Site",
    )
    DELETE = Endpoint(
        path="/Site/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Site/{id}",
        method="GET",
        summary="Get one Site",
        description="Use this to return a single instance of Site. Requires authentication.",
        path_params=["id"],
        query_params=["client_override", "domain", "includeactivity", "includedetails", "issetup", "tickettype_id"],
        response_model="Site",
    )
    LIST = Endpoint(
        path="/Site",
        method="GET",
        summary="List of Site",
        description="Use this to return multiple Site. Requires authentication.",
        query_params=["activeinactive", "advanced_search", "azuresites", "client_id", "contract_id", "count", "exclude_internal", "gfisites", "idonly", "includeactive", "includeaddress", "includeinactive", "includenonstocklocations", "includenoorderstockbin", "includenotes", "includestocklocations", "include_custom_fields", "iscalendarfilter", "item_id_qty", "item_salesorder_id", "item_salesorder_line", "lastupdatefromdate", "lastupdatetodate", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "override_enablestockbins", "page_no", "page_size", "pageinate", "search", "site_id", "sitefields", "stocklocation", "toplevel_id", "user_override"],
        response_model="Site_View",
    )
    LIST_GET = Endpoint(
        path="/Site/StockBins",
        method="GET",
        response_model="Site_List",
    )


class Slack:
    CREATE = Endpoint(
        path="/Slack/Manifest",
        method="POST",
        request_model="CreateSlackManifest",
    )
    CREATE_POST = Endpoint(
        path="/Slack/Interactivity",
        method="POST",
    )


class Slackchatapp:
    CREATE = Endpoint(
        path="/SlackChatApp",
        method="POST",
        request_model="SlackChatApp",
    )
    DELETE = Endpoint(
        path="/SlackChatApp/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SlackChatApp/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SlackChatApp",
        method="GET",
    )


class Slackdetails:
    CREATE = Endpoint(
        path="/SlackDetails",
        method="POST",
        request_model="SlackDetails",
    )
    CREATE_POST = Endpoint(
        path="/SlackDetails/Uninstall",
        method="POST",
    )
    DELETE = Endpoint(
        path="/SlackDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SlackDetails/{id}",
        method="GET",
        summary="Get one SlackDetails",
        description="Use this to return a single instance of SlackDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/SlackDetails",
        method="GET",
        summary="List of SlackDetails",
        description="Use this to return multiple SlackDetails. Requires authentication.",
        query_params=["agent_id", "channel_name", "includedisabled", "includeenabled", "team_name"],
    )


class Snipeitdetails:
    CREATE = Endpoint(
        path="/SnipeITDetails",
        method="POST",
        request_model="SnipeITDetails",
    )
    DELETE = Endpoint(
        path="/SnipeITDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SnipeITDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SnipeITDetails",
        method="GET",
    )


class Snowdetails:
    CREATE = Endpoint(
        path="/SnowDetails",
        method="POST",
        request_model="SnowDetails",
    )
    DELETE = Endpoint(
        path="/SnowDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SnowDetails/{id}",
        method="GET",
        summary="Get one SnowDetails",
        description="Use this to return a single instance of SnowDetails. Requires authentication.",
        path_params=["id"],
        query_params=["doDecrypt", "includedetails"],
    )
    LIST = Endpoint(
        path="/SnowDetails",
        method="GET",
        summary="List of SnowDetails",
        description="Use this to return multiple SnowDetails. Requires authentication.",
        query_params=["includedetails"],
    )


class Softwarelicence:
    CREATE = Endpoint(
        path="/SoftwareLicence",
        method="POST",
        request_model="Licence_List",
    )
    DELETE = Endpoint(
        path="/SoftwareLicence/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SoftwareLicence/{id}",
        method="GET",
        summary="Get one Licence",
        description="Use this to return a single instance of Licence. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/SoftwareLicence",
        method="GET",
        summary="List of Licence",
        description="Use this to return multiple Licence. Requires authentication.",
        query_params=["client_id", "count", "includeinactive", "licence_type", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "site_id", "tenant_id", "toplevelid"],
    )


class Softwarelicencerole:
    LIST = Endpoint(
        path="/SoftwareLicenceRole",
        method="GET",
        summary="List of LicenceRole",
        description="Use this to return multiple LicenceRole. Requires authentication.",
        query_params=["softwarelicence_id"],
    )


class Sophos:
    LIST = Endpoint(
        path="/Sophos/Get",
        method="GET",
    )


class Sophosdetails:
    CREATE = Endpoint(
        path="/SophosDetails",
        method="POST",
        request_model="SophosDetails",
    )
    DELETE = Endpoint(
        path="/SophosDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SophosDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/SophosDetails",
        method="GET",
    )


class Status:
    CREATE = Endpoint(
        path="/Status",
        method="POST",
        request_model="TStatus",
    )
    DELETE = Endpoint(
        path="/Status/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Status/{id}",
        method="GET",
        summary="Get one TStatus",
        description="Use this to return a single instance of TStatus. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Status",
        method="GET",
        summary="List of TStatus",
        description="Use this to return multiple TStatus. Requires authentication.",
        query_params=["domain", "excludeclosed", "excludepending", "outcome_id", "showall", "showcounts", "showquickchangeoptions", "split_closed", "ticket_id", "ticket_id_firstchild", "ticketarea_id", "tickettype_group_id", "tickettype_id", "tickettype_ids", "type", "view_id"],
    )


class Stockbin:
    CREATE = Endpoint(
        path="/StockBin",
        method="POST",
        request_model="StockBin",
    )
    DELETE = Endpoint(
        path="/StockBin/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/StockBin/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/StockBin",
        method="GET",
    )


class Stocktrace:
    GET = Endpoint(
        path="/StockTrace/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/StockTrace",
        method="GET",
    )


class Streamoneiondetails:
    CREATE = Endpoint(
        path="/StreamOneIonDetails",
        method="POST",
        request_model="StreamOneIonDetails",
    )
    DELETE = Endpoint(
        path="/StreamOneIonDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/StreamOneIonDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/StreamOneIonDetails",
        method="GET",
    )


class Styleprofile:
    CREATE = Endpoint(
        path="/StyleProfile",
        method="POST",
        request_model="StyleProfile",
    )
    DELETE = Endpoint(
        path="/StyleProfile/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/StyleProfile/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/StyleProfile",
        method="GET",
    )


class Supplier:
    CREATE = Endpoint(
        path="/Supplier",
        method="POST",
        request_model="Company",
        response_model="Company",
    )
    DELETE = Endpoint(
        path="/Supplier/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Supplier/{id}",
        method="GET",
        summary="Get one Company",
        description="Use this to return a single instance of Company. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
        response_model="Company",
    )
    LIST = Endpoint(
        path="/Supplier",
        method="GET",
        summary="List of Company",
        description="Use this to return multiple Company. Requires authentication.",
        query_params=["activeinactive", "count", "idonly", "includeactive", "includeinactive", "kashflowtenantid", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "toplevel_id", "xerotenantid"],
        response_model="Company_View",
    )


class Suppliercontract:
    CREATE = Endpoint(
        path="/SupplierContract",
        method="POST",
        request_model="Contract",
        response_model="Contract",
    )
    CREATE_POST = Endpoint(
        path="/SupplierContract/NextRef",
        method="POST",
        request_model="Contract",
    )
    DELETE = Endpoint(
        path="/SupplierContract/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SupplierContract/{id}",
        method="GET",
        summary="Get one Contract",
        description="Use this to return a single instance of Contract. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
        response_model="Contract",
    )
    LIST = Endpoint(
        path="/SupplierContract",
        method="GET",
        summary="List of Contract",
        description="Use this to return multiple Contract. Requires authentication.",
        query_params=["count", "includeinactive", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "search", "supplier_id"],
        response_model="Contract_View",
    )


class Synnexdetails:
    CREATE = Endpoint(
        path="/SynnexDetails",
        method="POST",
        request_model="SynnexDetails",
    )
    DELETE = Endpoint(
        path="/SynnexDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/SynnexDetails/{id}",
        method="GET",
        summary="Get one IngramMicroDetails",
        description="Use this to return a single instance of IngramMicroDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/SynnexDetails",
        method="GET",
    )


class Tabs:
    CREATE = Endpoint(
        path="/Tabs",
        method="POST",
        request_model="Tabname",
    )
    DELETE = Endpoint(
        path="/Tabs/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Tabs/{id}",
        method="GET",
        summary="Get one Tabname",
        description="Use this to return a single instance of Tabname. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Tabs",
        method="GET",
        summary="List of Tabname",
        description="Use this to return multiple Tabname. Requires authentication.",
        query_params=["type", "typeid"],
    )


class Tags:
    CREATE = Endpoint(
        path="/Tags",
        method="POST",
        request_model="Tag",
    )
    DELETE = Endpoint(
        path="/Tags/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Tags/{id}",
        method="GET",
        summary="Get one Tag",
        description="Use this to return a single instance of Tag. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Tags",
        method="GET",
    )


class Takecontrol:
    LIST = Endpoint(
        path="/TakeControl/GetUrl",
        method="GET",
        request_model="Control",
    )


class Taniumdetails:
    CREATE = Endpoint(
        path="/TaniumDetails",
        method="POST",
        request_model="TaniumDetails",
    )
    DELETE = Endpoint(
        path="/TaniumDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TaniumDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/TaniumDetails",
        method="GET",
    )


class Taskmonitorevent:
    LIST = Endpoint(
        path="/TaskMonitorEvent",
        method="GET",
    )


class Taskschedule:
    CREATE = Endpoint(
        path="/TaskSchedule",
        method="POST",
    )
    LIST = Endpoint(
        path="/TaskSchedule",
        method="GET",
    )


class Tasktrace:
    GET = Endpoint(
        path="/TaskTrace/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/TaskTrace",
        method="GET",
    )


class Tax:
    CREATE = Endpoint(
        path="/Tax",
        method="POST",
        request_model="Tax",
    )
    DELETE = Endpoint(
        path="/Tax/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Tax/{id}",
        method="GET",
        summary="Get one Tax",
        description="Use this to return a single instance of Tax. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "includeqbotaxrates"],
    )
    LIST = Endpoint(
        path="/Tax",
        method="GET",
        summary="List of Tax",
        description="Use this to return multiple Tax. Requires authentication.",
        query_params=["kashflowtenantid", "qbocompanyid", "related_to", "xerotenantid"],
    )


class Taxrule:
    CREATE = Endpoint(
        path="/TaxRule",
        method="POST",
        request_model="TaxRule",
    )
    DELETE = Endpoint(
        path="/TaxRule/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TaxRule/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/TaxRule",
        method="GET",
    )


class Team:
    CREATE = Endpoint(
        path="/Team",
        method="POST",
        request_model="SectionDetail",
    )
    DELETE = Endpoint(
        path="/Team/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Team/{id}",
        method="GET",
        summary="Get one SectionDetail",
        description="Use this to return a single instance of SectionDetail. Requires authentication.",
        path_params=["id"],
        query_params=["includeagents", "includedetails"],
    )
    LIST = Endpoint(
        path="/Team",
        method="GET",
        summary="List of SectionDetail",
        description="Use this to return multiple SectionDetail. Requires authentication.",
        query_params=["can_edit_only", "chat_only", "department_id", "domain", "ids", "include_managers", "includeagentsforteams", "includedisabled", "includeenabled", "istree", "memberonly", "mydeps", "myteamsonly", "orderbyseq", "outcome_id", "showall", "showcounts", "ticketarea_id", "type", "view_id"],
    )
    LIST_GET = Endpoint(
        path="/Team/Tree",
        method="GET",
    )


class Teamimage:
    GET = Endpoint(
        path="/TeamImage/{id}",
        method="GET",
        path_params=["id"],
    )


class Techdataresellerdetails:
    CREATE = Endpoint(
        path="/TechDataResellerDetails",
        method="POST",
        request_model="TechDataResellerDetails",
    )
    DELETE = Endpoint(
        path="/TechDataResellerDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TechDataResellerDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/TechDataResellerDetails",
        method="GET",
    )


class Template:
    CREATE = Endpoint(
        path="/Template",
        method="POST",
        request_model="StdRequest",
    )
    DELETE = Endpoint(
        path="/Template/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Template/{id}",
        method="GET",
        summary="Get one StdRequest",
        description="Use this to return a single instance of StdRequest. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "includekbinfo"],
    )
    LIST = Endpoint(
        path="/Template",
        method="GET",
        summary="List of StdRequest",
        description="Use this to return multiple StdRequest. Requires authentication.",
        query_params=["access_control_level", "action_id", "agent_id", "anonanduser", "asset_id", "client_id", "department_id", "domain", "group_id", "include_ticket_id", "includeclients", "includenames", "itil_ticket_type_id", "itil_type", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "parent_template_id", "report_id", "search", "showall", "team_id", "ticket_type_id", "todo_client_id", "todo_only", "type", "types"],
    )


class Tenable:
    CREATE = Endpoint(
        path="/Tenable/Export",
        method="POST",
        request_model="TenableCreateExport",
    )
    CREATE_POST = Endpoint(
        path="/Tenable/Cancel",
        method="POST",
    )
    LIST = Endpoint(
        path="/Tenable/Get",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/Tenable/Status",
        method="GET",
    )


class Tenabledetails:
    CREATE = Endpoint(
        path="/TenableDetails",
        method="POST",
        request_model="TenableDetails",
    )
    DELETE = Endpoint(
        path="/TenableDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TenableDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/TenableDetails",
        method="GET",
    )


class Tenant:
    CREATE = Endpoint(
        path="/Tenant",
        method="POST",
    )
    LIST = Endpoint(
        path="/Tenant",
        method="GET",
    )


class Test1:
    LIST = Endpoint(
        path="/Test1",
        method="GET",
    )


class Test3:
    LIST = Endpoint(
        path="/Test3",
        method="GET",
    )


class Test4:
    LIST = Endpoint(
        path="/Test4",
        method="GET",
    )


class Testerror:
    LIST = Endpoint(
        path="/TestError",
        method="GET",
    )


class Ticketapproval:
    CREATE = Endpoint(
        path="/TicketApproval",
        method="POST",
        request_model="FaultApproval",
    )
    DELETE = Endpoint(
        path="/TicketApproval/{id}&{seq}",
        method="DELETE",
        path_params=["id", "seq"],
    )
    GET = Endpoint(
        path="/TicketApproval/{id}",
        method="GET",
        summary="Get one FaultApproval",
        description="Use this to return a single instance of FaultApproval. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/TicketApproval",
        method="GET",
        summary="List of FaultApproval",
        description="Use this to return multiple FaultApproval. Requires authentication.",
        query_params=["action_number", "include_agent_details", "include_attachments", "includeapprovaldetails", "mine", "ticket_id"],
    )


class Ticketarea:
    CREATE = Endpoint(
        path="/TicketArea",
        method="POST",
        request_model="TicketArea",
    )
    DELETE = Endpoint(
        path="/TicketArea/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TicketArea/{id}",
        method="GET",
        summary="Get one TicketArea",
        description="Use this to return a single instance of TicketArea. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/TicketArea",
        method="GET",
    )


class Ticketrules:
    CREATE = Endpoint(
        path="/TicketRules",
        method="POST",
        request_model="Autoassign",
    )
    DELETE = Endpoint(
        path="/TicketRules/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TicketRules/{id}",
        method="GET",
        summary="Get one Autoassign",
        description="Use this to return a single instance of Autoassign. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/TicketRules",
        method="GET",
        summary="List of Autoassign",
        description="Use this to return multiple Autoassign. Requires authentication.",
        query_params=["access_control_level", "excludeworkflow", "includecriteriainfo", "isconfig", "rule_use"],
    )


class Tickettype:
    CREATE = Endpoint(
        path="/TicketType",
        method="POST",
        request_model="RequestType",
    )
    DELETE = Endpoint(
        path="/TicketType/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TicketType/{id}",
        method="GET",
        summary="Get one RequestType",
        description="Use this to return a single instance of RequestType. Requires authentication.",
        path_params=["id"],
        query_params=["can_create_only", "can_edit_only", "debug", "includeconfig", "includedetails", "includekbinfo", "includeteamrestrictions", "isdetailscreen", "isnewticket", "survey_fields", "ticket_id"],
    )
    LIST = Endpoint(
        path="/TicketType",
        method="GET",
        summary="List of RequestType",
        description="Use this to return multiple RequestType. Requires authentication.",
        query_params=["access_control_level", "anonanduser", "can_create_only", "can_edit_only", "canagentsselect", "canusercreate", "client_id", "domain", "group_id", "include_current", "include_mandatory_field_check", "isquicktimedropdown", "itil_type", "outcome_id", "searchtickets", "showall", "showcounts", "showinactive", "sprints_only", "ticketarea_id", "user_only", "view_id"],
    )


class Tickettypefield:
    LIST = Endpoint(
        path="/TicketTypeField",
        method="GET",
        summary="List of RequestTypeField",
        description="Use this to return multiple RequestTypeField. Requires authentication.",
        query_params=["buildcache", "debug", "isrtconfig"],
    )


class Tickettypegroup:
    CREATE = Endpoint(
        path="/TicketTypeGroup",
        method="POST",
        request_model="RequestTypeGroup",
    )
    DELETE = Endpoint(
        path="/TicketTypeGroup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TicketTypeGroup/{id}",
        method="GET",
        summary="Get one RequestTypeGroup",
        description="Use this to return a single instance of RequestTypeGroup. Requires authentication.",
        path_params=["id"],
        query_params=["getfields", "includedetails"],
    )
    LIST = Endpoint(
        path="/TicketTypeGroup",
        method="GET",
    )


class Tickets:
    CREATE = Endpoint(
        path="/Tickets",
        method="POST",
        request_model="Faults",
        response_model="Faults",
    )
    CREATE_POST = Endpoint(
        path="/Tickets/SetBillableProject",
        method="POST",
    )
    DELETE = Endpoint(
        path="/Tickets/{id}",
        method="DELETE",
        summary="Delete one Faults",
        description="Delete specific Faults. Requires authentication.",
        path_params=["id"],
        query_params=["reason"],
    )
    GET = Endpoint(
        path="/Tickets/{id}",
        method="GET",
        summary="Get one Faults",
        description="Use this to return a single instance of Faults. Requires authentication.",
        path_params=["id"],
        query_params=["amailentryid", "assignedto", "consignablelines", "debug", "dodatabaselookup", "email", "include_auditing", "includeagent", "includechildids", "includedetails", "includelastaction", "includelastappointment", "includelinkedobjects", "includenextappointment", "includeparentchangeinfo", "includeparentsubject", "includeseenby", "is_portal", "isdetailscreen", "ishalolink", "ispreview", "isteams", "nocache", "subject", "ticketidonly", "utcoffset"],
        response_model="Faults",
    )
    LIST = Endpoint(
        path="/Tickets",
        method="GET",
        summary="List of Faults",
        description="Use this to return multiple Faults. Requires authentication.",
        query_params=["advanced_search", "agent", "agent_id", "alerttype", "asset_id", "awaitinginput", "billableonly", "billing_date", "billing_type", "billingcontractid", "calendar_enddate", "calendar_startdate", "category_1", "category_2", "category_3", "category_4", "cf_display_values_only", "checkmyticketsonly", "client_id", "client_ids", "client_ref", "closed_only", "columns_id", "contract_id", "contract_period", "count", "datesearch", "debug", "default_columns", "deleted", "domain", "enddate", "enddatetime", "excludeslacalcs", "excludethese", "excludetickettypeallowall", "extraportalfilter", "facebook_id", "fetchgrandchildren", "flagged", "followedandagents", "ignoremilestonerestriction", "includeaccountmanager", "includeagent", "includeallopen", "includeappointmentid", "includeapproval", "includeassetkeyfield", "includeassettype", "includebreached", "includebudgettype", "includechildids", "includechildread", "includechildren", "includeclosed", "includecolumns", "includecompleted", "includecontract", "includecountryregion", "includefirstname", "include_custom_fields", "includefollowedonly", "includehold", "includeinactivetechs", "includeinactiveusers", "includeitilname", "includelastaction", "includelastincomingemail", "includelastname", "includelastnote", "includelocked", "includemailbox", "includemailid", "includemyuseronly", "includenextactivitydate", "includenextappointmenttype", "includeparentsubject", "includeprojects", "includeread", "includerelatedservices", "includerelease1", "includerelease2", "includerelease3", "includeservicecategory", "includeslaactiondate", "includeslatimer", "includestatus", "includesubmittedonly", "includesupplier", "includetickettype", "includetimetaken", "includetoplevel", "includeviewing", "includeworkflowstage", "includeworkflowstagenumber", "includuserdepartments", "inlcludeopenchildcount", "invlucebranch", "ismilestone", "isorion", "isquicktimesearch", "isscom", "isteams", "iszapier", "itil_requesttype", "itil_requesttype_id", "kanbanviewontheagentapp", "kanbanviewontheportal", "lastupdatefromdate", "lastupdatetodate", "list_id", "milestone_id", "mine", "nochargeonly", "notime", "onlytime", "open_only", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "orion_type", "page_no", "page_size", "pageinate", "parent_id", "pending_review", "per_action", "prepayorcontractonly", "priority", "product", "project_ids", "ready_for_invoicing", "related_id", "release_id", "requesttype", "requesttype_id", "requesttypegroup", "search", "search_details", "search_id", "search_inventory_number", "search_oppcompanyname", "search_oppcontactname", "search_oppemailaddress", "search_release1", "search_release2", "search_release3", "search_releasenote", "search_reportedby", "search_summary", "search_supplier_reference", "search_user_name", "search_version", "searchactions", "searchthisticketid", "service_id", "showonroadmap", "third_party_id", "third_party_id_string", "site_id", "sitepostcode", "sla", "sprint_for_tickettype_id", "sprints", "startandendset", "startdate", "startdatetime", "status", "status_id", "submittedandagents", "supplier_id", "supplier_status", "team", "team_name", "ticketarea_id", "ticketcontract_id", "ticketidonly", "ticketids", "ticketlinktype", "toplevel_id", "unlinked_only", "user_id", "username", "utcoffset", "view_id", "withattachments", "filetype_filter"],
        response_model="Faults_View",
    )
    LIST_GET = Endpoint(
        path="/Tickets/salesmailbox",
        method="GET",
    )


class Timesheet:
    CREATE = Endpoint(
        path="/Timesheet",
        method="POST",
        request_model="Timesheet",
    )
    GET = Endpoint(
        path="/Timesheet/{id}",
        method="GET",
        summary="Get one Timesheet",
        description="Use this to return a single instance of Timesheet. Requires authentication.",
        path_params=["id"],
        query_params=["agent_id", "date"],
    )
    LIST = Endpoint(
        path="/Timesheet",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/Timesheet/forecasting",
        method="GET",
    )


class Timesheetevent:
    CREATE = Endpoint(
        path="/TimesheetEvent",
        method="POST",
        request_model="TimesheetEvent",
    )
    DELETE = Endpoint(
        path="/TimesheetEvent/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TimesheetEvent/{id}",
        method="GET",
        summary="Get one TimesheetEvent",
        description="Use this to return a single instance of TimesheetEvent. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/TimesheetEvent",
        method="GET",
        summary="List of TimesheetEvent",
        description="Use this to return multiple TimesheetEvent. Requires authentication.",
        query_params=["agent_id", "agents", "end_date", "start_date", "utcoffset"],
    )
    LIST_GET = Endpoint(
        path="/TimesheetEvent/mine",
        method="GET",
    )


class Timeslot:
    LIST = Endpoint(
        path="/Timeslot",
        method="GET",
        summary="List of Timeslot",
        description="Use this to return multiple Timeslot. Requires authentication.",
        query_params=["agent_id", "workday_id"],
    )


class Todo:
    CREATE = Endpoint(
        path="/ToDo",
        method="POST",
        request_model="FaultToDo",
    )
    LIST = Endpoint(
        path="/ToDo",
        method="GET",
        summary="List of FaultToDo",
        description="Use this to return multiple FaultToDo. Requires authentication.",
        query_params=["ticket_id"],
    )


class Todogroup:
    CREATE = Endpoint(
        path="/ToDoGroup",
        method="POST",
        request_model="ToDoGroup",
    )
    DELETE = Endpoint(
        path="/ToDoGroup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ToDoGroup/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/ToDoGroup",
        method="GET",
    )


class Toplevel:
    CREATE = Endpoint(
        path="/TopLevel",
        method="POST",
        request_model="Tree",
    )
    DELETE = Endpoint(
        path="/TopLevel/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TopLevel/{id}",
        method="GET",
        summary="Get one Tree",
        description="Use this to return a single instance of Tree. Requires authentication.",
        path_params=["id"],
        query_params=["include_agents", "include_teams", "includedetails"],
    )
    LIST = Endpoint(
        path="/TopLevel",
        method="GET",
        summary="List of Tree",
        description="Use this to return multiple Tree. Requires authentication.",
        query_params=["agent_departments_only", "can_edit_only", "count", "idonly", "include_agents", "include_managers", "include_teams", "isorgchart", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "org_id", "page_no", "page_size", "pageinate", "search", "show_all", "type"],
    )


class Transcriptionstore:
    CREATE = Endpoint(
        path="/TranscriptionStore",
        method="POST",
        request_model="TranscriptionStore",
    )
    DELETE = Endpoint(
        path="/TranscriptionStore/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TranscriptionStore/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/TranscriptionStore",
        method="GET",
    )


class Translation:
    CREATE = Endpoint(
        path="/Translation",
        method="POST",
        request_model="LanguagePackTranslationsCustom",
    )
    LIST = Endpoint(
        path="/Translation",
        method="GET",
    )


class Twilio:
    CREATE = Endpoint(
        path="/Twilio/callback",
        method="POST",
        query_params=["guid"],
    )
    CREATE_POST = Endpoint(
        path="/Twilio/twiml",
        method="POST",
        query_params=["guid"],
    )


class Twiliodetails:
    LIST = Endpoint(
        path="/TwilioDetails",
        method="GET",
    )


class Twiliowhatsappdetails:
    CREATE = Endpoint(
        path="/TwilioWhatsAppDetails",
        method="POST",
        request_model="TwilioWhatsAppDetails",
    )
    DELETE = Endpoint(
        path="/TwilioWhatsAppDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TwilioWhatsAppDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/TwilioWhatsAppDetails",
        method="GET",
    )


class Twitterdetails:
    CREATE = Endpoint(
        path="/TwitterDetails",
        method="POST",
        request_model="TwitterDetails",
    )
    DELETE = Endpoint(
        path="/TwitterDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/TwitterDetails/{id}",
        method="GET",
        summary="Get one TwitterDetails",
        description="Use this to return a single instance of TwitterDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/TwitterDetails",
        method="GET",
        summary="List of TwitterDetails",
        description="Use this to return multiple TwitterDetails. Requires authentication.",
        query_params=["account_id"],
    )


class Unsubserviceemails:
    CREATE = Endpoint(
        path="/UnsubServiceEmails",
        method="POST",
        request_model="UnsubEmailServiceUsers",
    )
    DELETE = Endpoint(
        path="/UnsubServiceEmails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/UnsubServiceEmails/{id}",
        method="GET",
        summary="Get one UnsubEmailServiceUsers",
        description="Use this to return a single instance of UnsubEmailServiceUsers. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/UnsubServiceEmails",
        method="GET",
    )


class Userchange:
    LIST = Endpoint(
        path="/UserChange",
        method="GET",
        summary="List of UserChange",
        description="Use this to return multiple UserChange. Requires authentication.",
        query_params=["change_date", "count", "exclude_generaluser", "idonly", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate"],
    )


class Userroles:
    CREATE = Endpoint(
        path="/UserRoles",
        method="POST",
        request_model="UserRoles",
    )
    DELETE = Endpoint(
        path="/UserRoles/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/UserRoles/{id}",
        method="GET",
        summary="Get one UserRoles",
        description="Use this to return a single instance of UserRoles. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/UserRoles",
        method="GET",
    )


class Users:
    CREATE = Endpoint(
        path="/Users",
        method="POST",
        request_model="Users",
        response_model="Users",
    )
    CREATE_POST = Endpoint(
        path="/Users/prefs",
        method="POST",
        request_model="UserPrefs",
    )
    DELETE = Endpoint(
        path="/Users/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Users/{id}",
        method="GET",
        summary="Get one Users",
        description="Use this to return a single instance of Users. Requires authentication.",
        path_params=["id"],
        query_params=["client_id", "client_override", "domain", "includeactivity", "includebillinginfo", "includedetails", "includepopups", "includeusersassets", "issetup", "opp_id", "site_id", "site_override", "supplier_id", "tickettype_id", "username"],
        response_model="Users",
    )
    LIST = Endpoint(
        path="/Users",
        method="GET",
        summary="List of Users",
        description="Use this to return multiple Users. Requires authentication.",
        query_params=["activeinactive", "advanced_search", "allapprovers", "approvers_only", "asset_id", "client_id", "contract_id", "count", "department_id", "exclude_agents", "exclude_defaultsiteusers", "exclude_generaluser", "idonly", "includeactive", "includebillinginfo", "include_custom_fields", "includeinactive", "includename", "includenonserviceaccount", "includenotes", "includeserviceaccount", "integration_type", "is_followers", "is3cxcall", "lastupdatefromdate", "lastupdatetodate", "licence_id", "listagentuserfirst", "myallcustomers", "myarea", "mydepartment", "mysite", "mysitecontact", "mytoplevel", "opp_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "organisation_id", "page_no", "page_size", "pageinate", "role", "search", "search_phonenumbers", "site_id", "supplier_id", "tickettype_id", "toplevel_id", "linked_to_user_id"],
        response_model="Users_View",
    )
    LIST_GET = Endpoint(
        path="/Users/me",
        method="GET",
        response_model="Users",
    )


class Vmworkspacedetails:
    CREATE = Endpoint(
        path="/VMWorkspaceDetails",
        method="POST",
        request_model="VMWorkspaceDetails",
    )
    DELETE = Endpoint(
        path="/VMWorkspaceDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/VMWorkspaceDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/VMWorkspaceDetails",
        method="GET",
    )


class Versioninfo:
    GET = Endpoint(
        path="/VersionInfo/{id}",
        method="GET",
        summary="Get one Release",
        description="Use this to return a single instance of Release. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    GET_GET = Endpoint(
        path="/VersionInfo/GetOneSpotlight/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/VersionInfo",
        method="GET",
        description=". Requires authentication.",
        query_params=["product_id"],
    )
    LIST_GET = Endpoint(
        path="/VersionInfo/IntegratorHash",
        method="GET",
    )


class Viewcolumns:
    CREATE = Endpoint(
        path="/ViewColumns",
        method="POST",
        request_model="ViewColumns",
    )
    DELETE = Endpoint(
        path="/ViewColumns/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ViewColumns/{id}",
        method="GET",
        summary="Get one ViewColumns",
        description="Use this to return a single instance of ViewColumns. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ViewColumns",
        method="GET",
        summary="List of ViewColumns",
        description="Use this to return multiple ViewColumns. Requires authentication.",
        query_params=["globalonly", "showall", "showallforteam", "showallfortech", "ticketarea_id", "type"],
    )


class Viewfilter:
    CREATE = Endpoint(
        path="/ViewFilter",
        method="POST",
        request_model="ViewFilter",
    )
    DELETE = Endpoint(
        path="/ViewFilter/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ViewFilter/{id}",
        method="GET",
        summary="Get one ViewFilter",
        description="Use this to return a single instance of ViewFilter. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ViewFilter",
        method="GET",
        summary="List of ViewFilter",
        description="Use this to return multiple ViewFilter. Requires authentication.",
        query_params=["globalonly", "showall", "showallforteam", "showallfortech", "ticketarea_id", "type"],
    )


class Viewlistgroup:
    CREATE = Endpoint(
        path="/ViewListGroup",
        method="POST",
        request_model="ViewListGroup",
    )
    DELETE = Endpoint(
        path="/ViewListGroup/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ViewListGroup/{id}",
        method="GET",
        summary="Get one ViewListGroup",
        description="Use this to return a single instance of ViewListGroup. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/ViewListGroup",
        method="GET",
        summary="List of ViewListGroup",
        description="Use this to return multiple ViewListGroup. Requires authentication.",
        query_params=["type"],
    )


class Viewlists:
    CREATE = Endpoint(
        path="/ViewLists",
        method="POST",
        request_model="ViewLists",
    )
    DELETE = Endpoint(
        path="/ViewLists/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/ViewLists/{id}",
        method="GET",
        summary="Get one ViewLists",
        description="Use this to return a single instance of ViewLists. Requires authentication.",
        path_params=["id"],
        query_params=["domain", "includedetails", "showcounts"],
    )
    LIST = Endpoint(
        path="/ViewLists",
        method="GET",
        summary="List of ViewLists",
        description="Use this to return multiple ViewLists. Requires authentication.",
        query_params=["connectedinstance_id", "domain", "globalonly", "istree", "showall", "showallforteam", "showallfortech", "showcounts", "ticketarea_id", "type"],
    )


class Virima:
    LIST = Endpoint(
        path="/Virima/Get",
        method="GET",
    )


class Virimadetails:
    CREATE = Endpoint(
        path="/VirimaDetails",
        method="POST",
        request_model="VirimaDetails",
    )
    DELETE = Endpoint(
        path="/VirimaDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/VirimaDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/VirimaDetails",
        method="GET",
    )


class Virtualagent:
    CREATE = Endpoint(
        path="/VirtualAgent",
        method="POST",
        request_model="VirtualAgent",
    )
    DELETE = Endpoint(
        path="/VirtualAgent/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/VirtualAgent/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/VirtualAgent",
        method="GET",
    )


class Vorboss:
    LIST = Endpoint(
        path="/Vorboss/Get",
        method="GET",
    )


class Webhook:
    CREATE = Endpoint(
        path="/Webhook",
        method="POST",
        request_model="Webhook",
    )
    DELETE = Endpoint(
        path="/Webhook/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Webhook/{id}",
        method="GET",
        summary="Get one Webhook",
        description="Use this to return a single instance of Webhook. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Webhook",
        method="GET",
        summary="List of Webhook",
        description="Use this to return multiple Webhook. Requires authentication.",
        query_params=["isazureautomation", "type"],
    )


class Webhookevent:
    CREATE = Endpoint(
        path="/WebhookEvent",
        method="POST",
        request_model="WebhookEvent",
    )
    GET = Endpoint(
        path="/WebhookEvent/{id}",
        method="GET",
        summary="Get one WebhookEvent",
        description="Use this to return a single instance of WebhookEvent. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/WebhookEvent",
        method="GET",
        summary="List of WebhookEvent",
        description="Use this to return multiple WebhookEvent. Requires authentication.",
        query_params=["automation_id", "count", "idonly", "integrationmethod_id", "order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "webhook_id"],
    )


class Webhookrepository:
    GET = Endpoint(
        path="/WebhookRepository/{id}",
        method="GET",
        summary="Get one Webhook",
        description="Use this to return a single instance of Webhook. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/WebhookRepository",
        method="GET",
        summary="List of Webhook",
        description="Use this to return multiple Webhook. Requires authentication.",
        query_params=["isazureautomation", "type"],
    )


class Whatsapp:
    LIST = Endpoint(
        path="/WhatsApp/Get/Data",
        method="GET",
    )
    LIST_GET = Endpoint(
        path="/WhatsApp/Get/ProcessedIds",
        method="GET",
    )


class Wordpressdetails:
    CREATE = Endpoint(
        path="/WordpressDetails",
        method="POST",
        request_model="WordpressDetails",
    )
    DELETE = Endpoint(
        path="/WordpressDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/WordpressDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/WordpressDetails",
        method="GET",
    )


class Wordpressorgdetails:
    CREATE = Endpoint(
        path="/WordpressOrgDetails",
        method="POST",
        request_model="WordpressOrgDetails",
    )
    DELETE = Endpoint(
        path="/WordpressOrgDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/WordpressOrgDetails/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/WordpressOrgDetails",
        method="GET",
    )


class Workday:
    CREATE = Endpoint(
        path="/Workday",
        method="POST",
        request_model="Workdays",
    )
    DELETE = Endpoint(
        path="/Workday/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Workday/{id}",
        method="GET",
        summary="Get one Workdays",
        description="Use this to return a single instance of Workdays. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Workday",
        method="GET",
        summary="List of Workdays",
        description="Use this to return multiple Workdays. Requires authentication.",
        query_params=["access_control_level", "isconfig", "showholidays"],
    )


class Workflow:
    CREATE = Endpoint(
        path="/Workflow",
        method="POST",
        request_model="FlowHeader",
    )
    DELETE = Endpoint(
        path="/Workflow/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/Workflow/{id}",
        method="GET",
        summary="Get one FlowHeader",
        description="Use this to return a single instance of FlowHeader. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/Workflow",
        method="GET",
        summary="List of FlowHeader",
        description="Use this to return multiple FlowHeader. Requires authentication.",
        query_params=["access_control_level", "includeinactive"],
    )


class Workflowtarget:
    CREATE = Endpoint(
        path="/WorkflowTarget",
        method="POST",
        request_model="WorkflowTarget",
    )
    DELETE = Endpoint(
        path="/WorkflowTarget/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/WorkflowTarget/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/WorkflowTarget",
        method="GET",
    )


class Xerodetails:
    CREATE = Endpoint(
        path="/XeroDetails",
        method="POST",
        request_model="XeroDetails",
    )
    DELETE = Endpoint(
        path="/XeroDetails/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/XeroDetails/{id}",
        method="GET",
        summary="Get one XeroDetails",
        description="Use this to return a single instance of XeroDetails. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/XeroDetails",
        method="GET",
        summary="List of XeroDetails",
        description="Use this to return multiple XeroDetails. Requires authentication.",
        query_params=["connectedonly", "tenantid"],
    )


class Xtyperole:
    LIST = Endpoint(
        path="/XtypeRole",
        method="GET",
        summary="List of XTypeRole",
        description="Use this to return multiple XTypeRole. Requires authentication.",
        query_params=["xtype_id", "xtyperole_id"],
    )


class Zendesk:
    LIST = Endpoint(
        path="/Zendesk/Get",
        method="GET",
    )


class Zoom:
    CREATE = Endpoint(
        path="/Zoom/Message",
        method="POST",
        request_model="ZoomCreateMessageRequest",
    )


class Azureadconnection:
    CREATE = Endpoint(
        path="/azureadconnection",
        method="POST",
        request_model="AzureADConnection",
    )
    DELETE = Endpoint(
        path="/azureadconnection/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/azureadconnection/{id}",
        method="GET",
        summary="Get one AzureADConnection",
        description="Use this to return a single instance of AzureADConnection. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "includetenants"],
    )
    LIST = Endpoint(
        path="/azureadconnection",
        method="GET",
        summary="List of AzureADConnection",
        description="Use this to return multiple AzureADConnection. Requires authentication.",
        query_params=["authorized", "isintune", "type", "types"],
    )


class Azureadmapping:
    LIST = Endpoint(
        path="/azureadmapping",
        method="GET",
        summary="List of AzureADMapping",
        description="Use this to return multiple AzureADMapping. Requires authentication.",
        query_params=["connection_id"],
    )


class Cspinvoice:
    CREATE = Endpoint(
        path="/cspinvoice",
        method="POST",
        request_model="CSPInvoice",
    )
    DELETE = Endpoint(
        path="/cspinvoice/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/cspinvoice/{id}",
        method="GET",
        path_params=["id"],
    )
    LIST = Endpoint(
        path="/cspinvoice",
        method="GET",
    )


class Formattedemail:
    CREATE = Endpoint(
        path="/formattedemail",
        method="POST",
        request_model="FormattedEmail",
    )
    DELETE = Endpoint(
        path="/formattedemail/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/formattedemail/{id}",
        method="GET",
        summary="Get one formattedemail",
        description="Use this to return a single instance of formattedemail. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/formattedemail",
        method="GET",
    )


class Incomingemail:
    CREATE = Endpoint(
        path="/incomingemail",
        method="POST",
        request_model="IncomingEmail",
    )
    CREATE_POST = Endpoint(
        path="/incomingemail/AddToTicket",
        method="POST",
        request_model="AddToTicket",
    )
    DELETE = Endpoint(
        path="/incomingemail/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/incomingemail/{id}",
        method="GET",
        summary="Get one IncomingEmail",
        description="Use this to return a single instance of IncomingEmail. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails", "showcurrentagentonly"],
    )
    LIST = Endpoint(
        path="/incomingemail",
        method="GET",
        summary="List of IncomingEmail",
        description="Use this to return multiple IncomingEmail. Requires authentication.",
        query_params=["order", "order2", "order3", "order4", "order5", "orderdesc", "orderdesc2", "orderdesc3", "orderdesc4", "orderdesc5", "page_no", "page_size", "pageinate", "showcurrentagentonly"],
    )


class Itemsupplier:
    CREATE = Endpoint(
        path="/itemsupplier",
        method="POST",
        request_model="ItemSupplier",
    )
    DELETE = Endpoint(
        path="/itemsupplier/{id}",
        method="DELETE",
        path_params=["id"],
    )
    GET = Endpoint(
        path="/itemsupplier/{id}",
        method="GET",
        summary="Get one ItemSupplier",
        description="Use this to return a single instance of ItemSupplier. Requires authentication.",
        path_params=["id"],
        query_params=["includedetails"],
    )
    LIST = Endpoint(
        path="/itemsupplier",
        method="GET",
    )


class Mcp:
    CREATE = Endpoint(
        path="/mcp",
        method="POST",
    )
    DELETE = Endpoint(
        path="/mcp",
        method="DELETE",
    )
    LIST = Endpoint(
        path="/mcp",
        method="GET",
    )


class Pagerdutymapping:
    LIST = Endpoint(
        path="/pagerdutymapping",
        method="GET",
        summary="List of PagerDutyMapping",
        description="Use this to return multiple PagerDutyMapping. Requires authentication.",
        query_params=["service_id"],
    )


class Workflowstep:
    LIST = Endpoint(
        path="/workflowstep",
        method="GET",
        summary="List of FlowDetail",
        description="Use this to return multiple FlowDetail. Requires authentication.",
        query_params=["includecriteriainfo"],
    )

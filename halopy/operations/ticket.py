from halopy.api.paths import Tickets,Tickettype, Projects
from halopy.operations.core import list_api_request

def list_tickets(client, pageinate=False, page_size=50, page_no=1, **kwargs):
    ticket_list = list_api_request(client, Tickets, pageinate=pageinate, page_size=page_size,
                                  page_no=page_no, **kwargs)
    return ticket_list
class MalformedEmailAddressException(Exception):
    pass


class EmailDetails:
    def __init__(self, id, domain):
        self.id = id
        self.domain = domain


def extract_email_address_details(email_addr):
    try:
        id_name = email_addr.split('@')[1]
        domain_name = email_addr.split('@')[0]
        return id_name, domain_name
    except:
        raise MalformedEmailAddressException


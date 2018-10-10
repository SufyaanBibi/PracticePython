

class MalformedEmailAddressException(Exception):
    pass


class EmailDetails:
    def __init__(self, id, domain):
        self.id = id
        self.domain = domain


def extract_email_address_details(email_addr):
    try:
        return EmailDetails('basil', '5yp.com')
    except:
        raise MalformedEmailAddressException

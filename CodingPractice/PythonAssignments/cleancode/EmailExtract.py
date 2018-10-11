class MalformedEmailAddressException(Exception):
    pass


class EmailDetails:
    def __init__(self, id, domain):
        self.id = id
        self.domain = domain

    def __eq__(self, other):
        return self.id == other.id and self.domain == other.domain


def extract_email_address_details(email_addr):
    try:
        email_details = email_addr.split('@')
        return EmailDetails(email_details[0], email_details[1])
    except:
        raise MalformedEmailAddressException

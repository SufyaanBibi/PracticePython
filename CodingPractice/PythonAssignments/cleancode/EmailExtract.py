class MalformedEmailAddressException(Exception):
    pass


class EmailDetails:
    def __init__(self, id, domain):
        self.id = id
        self.domain = domain


def extract_email_address_details(email_addr):
    try:
        email_details = email_addr.split('@')
        return EmailDetails(email_details[0], email_details[1])
    except:
        raise MalformedEmailAddressException

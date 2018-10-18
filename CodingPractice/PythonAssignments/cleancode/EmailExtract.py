import re


class MalformedEmailAddressException(Exception):
    pass


class EmailDetails:
    def __init__(self, id, domain):
        self.id = id
        self.domain = domain

    def __eq__(self, other):
        return self.id == other.id and self.domain == other.domain

    def get_id(self):
        return self.id

    def get_domain(self):
        return self.domain


def extract_email_address_details(email_addr):
    try:
        if not re.match(r'[^@,\s+]+@[^@,\s+]+\.[^@,\s+]+', email_addr):
            raise MalformedEmailAddressException(email_addr)
        email_details = email_addr.split('@')
        email_id, domain = email_details
        return EmailDetails(email_id, domain)
    except:
        raise MalformedEmailAddressException(email_addr)

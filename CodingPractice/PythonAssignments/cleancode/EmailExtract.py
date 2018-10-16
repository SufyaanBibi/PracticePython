import re


class MalformedEmailAddressException(Exception):
    pass


class EmailDetails:
    def __init__(self, _id, _domain):
        self.id = _id
        self.domain = _domain

    def __eq__(self, other):
        return self.id == other.id and self.domain == other.domain

    def get_id(self):
        return self.id

    def get_domain(self):
        return self.domain


def extract_email_address_details(email_addr):
    try:
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email_addr):
            raise MalformedEmailAddressException('This is an invalid email address')
        email_details = email_addr.split('@')
        return EmailDetails(email_details[0], email_details[1])
    except:
        raise MalformedEmailAddressException('This is an invalid email address.')

import re


class MalformedEmailAddressException(Exception):
    pass


class EmailDetails:
    def __init__(self, local_part, domain):
        self._local_part = local_part
        self._domain = domain

    def __eq__(self, other):
        return self._local_part == other._local_part and self._domain == other._domain

    def get_id(self):
        return self._local_part

    def get_domain(self):
        return self._domain


def extract_email_address_details(email_addr):
    pattern = re.compile('[^@,]+'
                         '@'
                         '[^@,.]+'
                         '\.'
                         '[^@,.]+')
    try:
        if re.match(pattern, email_addr):
            email_id, domain = email_addr.split('@')
            return EmailDetails(email_id, domain)

        raise MalformedEmailAddressException(email_addr)

    except MalformedEmailAddressException:
        raise
    except Exception:
        raise MalformedEmailAddressException(email_addr)

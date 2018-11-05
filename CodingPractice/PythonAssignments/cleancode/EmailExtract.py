import re


class MalformedEmailAddressException(Exception):
    def __init__(self, message):
        self.message = message


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


def email_length_constraint(local_part):
    if len(local_part) > 64:
        raise MalformedEmailAddressException(f'{local_part} exceeds length constraint: 64 characters.')


def is_invalid_single_quote(local_part):
    r = re.search(r'"[^"]*$', local_part)
    print(r)
    if r:
        return True
    else:
        return False


def extract_email_address_details(email_addr):
    pattern = re.compile('[^@,]+'
                         '@'
                         '[^@,.]+'
                         '\.'
                         '[^@,.]+')
    try:
        if re.match(pattern, email_addr):
            local_part, domain = email_addr.split('@')
            email_length_constraint(local_part)
            invalid_single_quote(local_part)
            return EmailDetails(local_part, domain)

        raise MalformedEmailAddressException(email_addr)

    except MalformedEmailAddressException:
        raise
    except Exception:
        raise MalformedEmailAddressException(email_addr)

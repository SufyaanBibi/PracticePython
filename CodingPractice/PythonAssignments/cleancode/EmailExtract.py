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


def double_quotes_validation(local_part):
    double_quotes = [e for e in local_part if e == '"']
    if len(double_quotes) == 0:
        return
    if len(double_quotes) == 2:
        if local_part[0] and local_part[-1] == '"':
            return
        else:
            raise MalformedEmailAddressException(f'{local_part} contains invalid double quotes.')
    else:
        raise MalformedEmailAddressException(f'{local_part} contains invalid double quotes.')


def multiple_dot_character_constraint(local_part):
    if re.search(r'.*[.]{2,}.*', local_part):
        raise MalformedEmailAddressException(f'{local_part} contains multiple dot characters adjacent to each other.')


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
            double_quotes_validation(local_part)
            multiple_dot_character_constraint(local_part)
            return EmailDetails(local_part, domain)

        raise MalformedEmailAddressException(email_addr)

    except MalformedEmailAddressException:
        raise
    except Exception:
        raise MalformedEmailAddressException(email_addr)

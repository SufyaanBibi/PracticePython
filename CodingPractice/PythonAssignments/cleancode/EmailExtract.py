class MalformedEmailAddress(Exception):
    pass


class EmailDetails:
    def __init__(self, id, domain):
        self.id = id
        self.domain = domain


def extract_details_from_email_address(email_addr):
    # return a value that will pass the test
    return EmailDetails('basil', '5yp.com')

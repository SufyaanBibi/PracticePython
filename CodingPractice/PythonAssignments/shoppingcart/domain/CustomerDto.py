
class CustomerDto:

    def __init__(self, customer_id, first_name, last_name, sex, age, birthday, email_address,
                 mail_shot_date, iso_country_code):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._sex = sex
        self._age = age
        self._birthday = birthday
        self._email_address = email_address
        self._mail_shot_date = mail_shot_date
        self._iso_country_code = iso_country_code

    def __eq__(self, other):
        return self._first_name == other._first_name and self._last_name and other._last_name \
               and self._sex == other._sex and self._age == other._age and self._customer_id == other._customer_id \
               and self._birthday == other._birthday and self._email_address == other._email_address and \
               self._mail_shot_date == other._mail_shot_date and self._iso_country_code == other._iso_country_code

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_sex(self):
        return self._sex

    def get_age(self):
        return self._age

    def get_customer_id(self):
        return self._customer_id

    def get_birth_date(self):
        return self._birthday

    def get_email_addr(self):
        return self._email_address

    def get_mail_shot_date(self):
        return self._mail_shot_date

    def get_iso_country_code(self):
        return self._iso_country_code

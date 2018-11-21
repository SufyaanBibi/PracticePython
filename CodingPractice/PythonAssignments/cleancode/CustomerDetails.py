
class CustomerDetails:

    def __init__(self, first_name, last_name, sex, age, cstmr_id, birthdt, email, mail_shot_dt, iso_cnty_code):
        self._first_name = first_name
        self._last_name = last_name
        self._sex = sex
        self._age = age
        self._cstmer_id = cstmr_id
        self._birthdt = birthdt
        self._email = email
        self._mail_shot_dt = mail_shot_dt
        self._iso_cnty_code = iso_cnty_code

    def __eq__(self, other):
        return self._first_name == other._first_name and self._last_name and other._last_name \
               and self._sex == other._sex and self._age == other._age and self._cstmer_id == other._cstmer_id \
               and self._birthdt == other._birthdt and self._email == other._email and self._mail_shot_dt == \
               other._mail_shot_dt and self._iso_cnty_code == other._iso_cnty_code

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_sex(self):
        return self._sex

    def get_age(self):
        return self._age

    def get_customer_id(self):
        return self._cstmer_id

    def get_birth_date(self):
        return self._birthdt

    def get_email_addr(self):
        return self._email

    def get_mail_shot_date(self):
        return self._mail_shot_dt

    def get_iso_country_code(self):
        return self._iso_cnty_code

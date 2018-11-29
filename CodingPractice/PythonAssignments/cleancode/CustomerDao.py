from abc import ABC, abstractmethod
import json
from CodingPractice.PythonAssignments.cleancode.CustomerDetailsDao import *


class CustomerDao(ABC):

    @abstractmethod
    def get_customers(self):
        return

    @abstractmethod
    def get_customer_by_id(self, customer_id):
        return

    @abstractmethod
    def get_customers_by_name(self, last_name, first_name):
        return

    @abstractmethod
    def get_customers_by_iso_country_code(self, iso_country_code):
        return


class CustomerJsonDao(CustomerDao):

    @staticmethod
    def _get_file_path(fn):
        import os
        return os.path.join(os.path.dirname(__file__), fn)

    @staticmethod
    def _get_json(file_name):
        fn = CustomerJsonDao._get_file_path(file_name)
        with open(fn, 'r') as f:
            return json.load(f)

    @staticmethod
    def _create_cust(c):
        return CustomerDetails(c["customer_id"], c["first_name"], c["last_name"], c["sex"],
                                   c["age"], c["birthday"], c["email_address"], c["mail_shot_date"],
                                   c["iso_country_code"])

    @staticmethod
    def make_customers_from_json(j):
        custs = []
        for cust in j["customers"]:
            custs.append(CustomerJsonDao._create_cust(cust))
        return custs

    def get_customers(self):
        jf = CustomerJsonDao._get_json('customers.json')
        return make_customers_from_json(jf)

    def get_customer_by_id(self, customer_id):
        custs = self.get_customers()
        return [cust for cust in custs if customer_id == cust.get_customer_id()][0]

    def get_customers_by_name(self, last_name, first_name):
        custs = self.get_customers()
        return [cust for cust in custs if last_name == cust.get_last_name() and first_name == cust.get_first_name()]

    def get_customers_by_iso_country_code(self, iso_country_code):
        custs = self.get_customers()
        return [cust for cust in custs if iso_country_code == cust.get_iso_country_code()]

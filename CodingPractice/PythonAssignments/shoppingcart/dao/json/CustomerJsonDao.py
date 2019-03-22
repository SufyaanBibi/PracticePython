from CodingPractice.PythonAssignments.shoppingcart.dao.json.JsonFileReader import JsonFileReader
from CodingPractice.PythonAssignments.shoppingcart.dao.CustomerDao import *
from CodingPractice.PythonAssignments.shoppingcart.dao.CustomerDetailsDao import *
from CodingPractice.PythonAssignments.shoppingcart.dao.json.MethodNotImplementedException import MethodNotImplementedException


class CustomerJsonDao(CustomerDao, JsonFileReader):

    @staticmethod
    def _create_cust(c):
        return CustomerDto(c["customer_id"], c["first_name"], c["last_name"], c["sex"],
                           c["age"], c["birthday"], c["email_address"], c["mail_shot_date"],
                           c["iso_country_code"])

    @staticmethod
    def _make_customers_from_json(j):
        custs = []
        for cust in j["customers"]:
            custs.append(CustomerJsonDao._create_cust(cust))
        return custs

    def __init__(self, json_file_path):
        self._json_file_path = json_file_path

    def get_customers(self):
        jf = CustomerJsonDao._get_json(self._json_file_path)
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

    def create_customer(self, customerDto):
        raise MethodNotImplementedException('create_customer called on CustomerJsonDao')

    def delete_customer(self, customerDto):
        raise MethodNotImplementedException('delete_customer called on CustomerJsonDao')

    def update_customer(self, customerDto):
        raise MethodNotImplementedException('update_customer called on CustomerJsonDao')

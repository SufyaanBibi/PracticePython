from abc import ABC, abstractmethod


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

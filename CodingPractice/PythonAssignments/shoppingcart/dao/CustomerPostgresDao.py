from contextlib import closing
from CodingPractice.PythonAssignments.shoppingcart.dao.CustomerDao import CustomerDao
from CodingPractice.PythonAssignments.shoppingcart.domain.CustomerDto import CustomerDto


class CustomerPostgresDao(CustomerDao):

    def __init__(self, postgres_conn):
        self._postgres_conn = postgres_conn
        
    @staticmethod
    def _create_cust_dto_from_row(row):
        return CustomerDto(customer_id=row[0], first_name=row[1], last_name=row[2], sex=row[3],
                           age=row[4], birthday=row[5], email_address=row[6], mail_shot_date=row[7],
                           iso_country_code=row[8])

    def get_customers(self):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute('SELECT * FROM CUSTOMER;')
            customers = cursor.fetchall()
            return [self._create_cust_dto_from_row(c) for c in customers]

    def get_customer_by_id(self, customer_id):
        return

    def get_customers_by_name(self, last_name, first_name):
        return

    def get_customers_by_iso_country_code(self, iso_country_code):
        return

    def create_customer(self, customerDto):
        return

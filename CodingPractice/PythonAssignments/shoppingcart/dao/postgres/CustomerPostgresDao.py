from contextlib import closing
import pg8000

from CodingPractice.PythonAssignments.shoppingcart.dao.CustomerDao import CustomerDao
from CodingPractice.PythonAssignments.shoppingcart.domain.CustomerDto import CustomerDto


class CustomerPostgresDao(CustomerDao):

    def __init__(self, postgres_instance):
        self._postgres_conn = pg8000.connect(**postgres_instance.dsn())

        
    @staticmethod
    def _create_cust_dto_from_row(row):
        return CustomerDto(customer_id=row[0], first_name=row[1], last_name=row[2], sex=row[3],
                           age=row[4], birthday=row[5], email_address=row[6], mail_shot_date=row[7],
                           iso_country_code=row[8])

    def _fetch_customers_with_sql(self, sql):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(sql)
            customers = cursor.fetchall()
            return [self._create_cust_dto_from_row(row) for row in customers]

    def get_customers(self):
        return self._fetch_customers_with_sql('SELECT * FROM customer;')

    def get_customer_by_id(self, customer_id):
        return self._fetch_customers_with_sql(f'SELECT * FROM customer WHERE customer_id={customer_id};')

    def get_customers_by_name(self, last_name, first_name):
        return self._fetch_customers_with_sql(
            "SELECT * FROM customer WHERE last_name='"+last_name+"' AND first_name='"+first_name+"';")

    def get_customers_by_iso_country_code(self, iso_country_code):
        return self._fetch_customers_with_sql("SELECT * FROM customer WHERE iso_country_code='"+iso_country_code+"';")

    def create_customer(self, customer_dto):
        return

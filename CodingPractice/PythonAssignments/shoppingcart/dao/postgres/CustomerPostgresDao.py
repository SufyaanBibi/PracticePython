from contextlib import closing
import pg8000

from CodingPractice.PythonAssignments.shoppingcart.dao.CustomerDao import CustomerDao
from CodingPractice.PythonAssignments.shoppingcart.domain.CustomerDto import CustomerDto


class CustomerPostgresDao(CustomerDao):

    def __init__(self, postgres_instance):
        self._postgres_conn = pg8000.connect(**postgres_instance.dsn())

    INSERT_SQL = '''INSERT INTO customer(customer_id, 
                    first_name,
                    last_name,
                    sex,
                    age,
                    birthday,
                    email_address,
                    mail_shot_date,
                    iso_country_code)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        
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
        custs = self._fetch_customers_with_sql(f'SELECT * FROM customer WHERE customer_id={customer_id};')
        if custs:
            return custs[0]

    def get_customers_by_name(self, last_name, first_name):
        return self._fetch_customers_with_sql(
            "SELECT * FROM customer WHERE last_name='"+last_name+"' AND first_name='"+first_name+"';")

    def get_customers_by_iso_country_code(self, iso_country_code):
        return self._fetch_customers_with_sql("SELECT * FROM customer WHERE iso_country_code='"+iso_country_code+"';")

    def create_customer(self, customer_dto):
        cust_tuple = (customer_dto.get_customer_id(),
                      customer_dto.get_first_name(),
                      customer_dto.get_last_name(),
                      customer_dto.get_sex(),
                      customer_dto.get_age(),
                      customer_dto.get_birthday(),
                      customer_dto.get_email_addr(),
                      customer_dto.get_mail_shot_date(),
                      customer_dto.get_iso_country_code())
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(self.INSERT_SQL, cust_tuple)

    def delete_customer(self, customerDto):
        customer_id = customerDto.get_customer_id()
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(f"DELETE FROM customer WHERE customer_id={customer_id};")

    def update_customer(self, customerDto):
        customer_id = customerDto.get_customer_id()
        first_name = customerDto.get_first_name()
        last_name = customerDto.get_last_name()
        sex = customerDto.get_sex()
        age = customerDto.get_age()
        birthday = customerDto.get_birthday()
        email_addr = customerDto.get_email_addr()
        mail_shot = customerDto.get_mail_shot_date()
        iso_country_code = customerDto.get_iso_country_code()
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(f"UPDATE customer \
                            SET first_name='{first_name}', last_name='{last_name}', sex='{sex}', age={age}, \
                            birthday='{birthday}', email_address='{email_addr}', mail_shot_date='{mail_shot}', \
                            iso_country_code='{iso_country_code}' \
                            WHERE customer_id={customer_id};"
                           )

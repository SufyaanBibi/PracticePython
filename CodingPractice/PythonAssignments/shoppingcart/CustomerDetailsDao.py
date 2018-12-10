from CodingPractice.PythonAssignments.shoppingcart.CustomerDto import CustomerDto


def create_cust(c):
    return CustomerDto(c["customer_id"], c["first_name"], c["last_name"], c["sex"],
                       c["age"], c["birthday"], c["email_address"], c["mail_shot_date"],
                       c["iso_country_code"])


def make_customers_from_json(j):
    custs = []
    for cust in j["customers"]:
        custs.append(create_cust(cust))
    return custs

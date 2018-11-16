import unittest
from CodingPractice.PythonAssignments.excercises.UniqueCustomerName import unique_customer_name


class UniqueFirstNameTests(unittest.TestCase):

    def test_00_unique_first_names(self):
        name_list = [('Alice', 'Wonderlund'), ('Sadie', 'Frost'), ('Sam', 'Antha'), ('Sadie', 'Lady')]
        self.assertEqual(3, unique_customer_name(name_list))

    def test_01_names_with_upper_and_lower_letters_Alice_and_alice(self):
        name_list = [('Alice', 'Wonderlund'), ('alice', 'Joy')]
        self.assertEqual(2, unique_customer_name(name_list))


if __name__ == '__main__':
    unittest.main()

import unittest
from CodingPractice.PythonAssignments.excercises.UniqueCustomerName import unique_customer_name


class UniqueFirstNameTests(unittest.TestCase):

    def test_00_unique_first_names(self):
        name_list = [ ('Alice', 'Wonderlund') , ('Sadie', 'Frost'), ('Sam', 'Antha'), ('Sadie', 'Lady') ]
        self.assertEqual(3, unique_customer_name(name_list))


if __name__ == '__main__':
    unittest.main()
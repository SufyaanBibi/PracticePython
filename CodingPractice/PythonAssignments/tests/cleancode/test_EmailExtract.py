import unittest
from CodingPractice.PythonAssignments.cleancode.EmailExtract \
    import EmailDetails, extract_email_address_details, MalformedEmailAddressException



class EmailExtractTests(unittest.TestCase):

    def test_00_is_id_valid(self):
        actual = extract_email_address_details( 'basil@5yp.com' )
        self.assertEqual('basil', actual.id)

    def test_01_can_extract_address(self):
        expected = EmailDetails('basil', '5yp.com')
        actual = extract_email_address_details( 'basil@5yp.com' )
        self.assertEqual(expected, actual)

    def test_02_exception_raised_for_malformed_email_address(self):
        with self.assertRaises(MalformedEmailAddressException):
            extract_email_address_details( 'BAD_EMAIL_ADDRESS' )


if __name__ == '__main__':
    unittest.main()

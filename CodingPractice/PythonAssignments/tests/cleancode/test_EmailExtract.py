# This file holds tests for the testing of the email address tests.

# import unuttest so we can do unit testing on email addresses
import unittest
from CodingPractice.PythonAssignments.cleancode.EmailExtract \
    import EmailDetails, extract_email_address_details, MalformedEmailAddressException


class EmailExtractTests(unittest.TestCase):

    # This tests that the name of the person in the email address has been done correctly.
    def test_is_id_valid(self):
        actual = extract_email_address_details( 'basil@5yp.com' )
        self.assertEqual('basil', actual.id)

    def test_can_extract_address(self):
        expected = EmailDetails('basil', '5yp.com')
        actual = extract_email_address_details( 'basil@5yp.com' )
        self.assertEqual(expected, actual)

    def test_exception_raised_for_malformed_email_address(self):
        with self.assertRaises(MalformedEmailAddressException):
            extract_email_address_details( 'BAD_EMAIL_ADDRESS' )


if __name__ == '__main__':
    unittest.main()

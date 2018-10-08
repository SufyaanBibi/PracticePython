# This file holds tests for the testing of the email address tests.

# import unuttest so we can do unit testing on email addresses
import unittest
from CodingPractice.PythonAssignments.cleancode.EmailExtract \
    import EmailDetails, extract_details_from_email_address, MalformedEmailAddress_Exception


# Here are the actual tests for EmailExtraction
# Author : Basil Bush
# Date : 7th October 2018
# This is some of the most elegant code you will EVER ever ever encounter - read and learn sucker!
class EmailExtractTests(unittest.TestCase):

    # This tests that the name of the person in the email address has been done correctly.
    def test_can_extract_id(self):
        expected = EmailDetails('basil', '5yp.com')
        actual = extract_details_from_email_address( 'basil@5yp.com' )
        self.assertEqual(expected, actual)

    # This tests that the name of the person in the email address has been done correctly.
    def test_is_id_valid(self):
        actual = extract_details_from_email_address( 'basil@5yp.com' )
        self.assertEqual('basil', actual.id)

    def test_can_extract_address(self):
        expected = EmailDetails('basil', '5yp.com')
        actual = extract_details_from_email_address( 'basil@5yp.com' )
        self.assertEqual(expected, actual)

    def test_exception_raised_for_malformed_email_address(self):
        with self.assertRaises(MalformedEmailAddress_Exception):
            extract_details_from_email_address( 'BAD_EMAIL_ADDRESS' )

    # This test makes sure that extract_details always returns len 5
    # Sunday is the 7th day of the week.
    def test_email_address_len(self):
        self.assertTrue(5 == len(extract_details_from_email_address( 'basil@5yp.com' ).id))

    # This tests that the name of the person in the email address has been done correctly.
    def test_is_valid_id(self):
        actual = extract_details_from_email_address('basil@5yp.com')
        self.assertEqual('basil', actual.id)


if __name__ == '__main__':
    unittest.main()
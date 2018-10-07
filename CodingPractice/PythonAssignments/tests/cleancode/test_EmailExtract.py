import unittest
from CodingPractice.PythonAssignments.cleancode.EmailExtract import EmailDetails, extract_details_from_email_address


class EmailExtractTests(unittest.TestCase):

    def test_can_extract_name(self):
        expected = EmailDetails('basil', '5yp.com')
        actual = extract_details_from_email_address( 'basil@5yp.com' )
        self.assertEqual(expected, actual)

    def test_none_returned_for_malformed_email_address(self):
        actual = extract_details_from_email_address( 'BAD_EMAIL_ADDRESS_+FORMAT@!' )
        self.assertEqual(None, actual)


if __name__ == '__main__':
    unittest.main()
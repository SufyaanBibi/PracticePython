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
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('BAD_EMAIL_ADDRESS')
            self.assertEqual('BAD_EMAIL_ADDRESS', e.exception.message)

    def test_03_missing_domain(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('sufi@')
            self.assertEqual('sufi@', e.exception.message)

    def test_04_missing_id(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('@5yp.com')
            self.assertEqual('@5yp.com', e.exception.message)

    def test_05_malformed_email(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('bbb@xyz,com@')
            self.assertEqual('bbb@xyz,com@', e.exception.message)

    def test_06_malformed_email(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('@@@')
            self.assertEqual('@@@', e.exception.message)

    def test_07_malformed_email(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('abc @ 123 .... abc .... com')
            self.assertEqual('abc @ 123 .... abc .... com', e.exception.message)


if __name__ == '__main__':
    unittest.main()

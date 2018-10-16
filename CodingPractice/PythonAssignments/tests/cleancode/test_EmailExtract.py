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
        with self.assertRaises(MalformedEmailAddressException) as cm:
            extract_email_address_details('BAD_EMAIL_ADDRESS').fail()
        self.assertEqual(
            'This is an invalid email address.',
            str(cm.exception)
        )

    def test_03_missing_domain(self):
        with self.assertRaises(MalformedEmailAddressException) as cm:
            extract_email_address_details('sufi@').fail()
        self.assertEqual(
            'This is an invalid email address.',
            str(cm.exception)
        )

    def test_04_missing_id(self):
        with self.assertRaises(MalformedEmailAddressException) as cm:
            extract_email_address_details('@5yp.com').fail()
        self.assertEqual(
            'This is an invalid email address.',
            str(cm.exception)
        )

    def test_05_malformed_email(self):
        with self.assertRaises(MalformedEmailAddressException) as cm:
            extract_email_address_details('bbb@xyz,com@').fail()
        self.assertEqual(
            'This is an invalid email address.',
            str(cm.exception)
        )

    def test_06_malformed_email(self):
        with self.assertRaises(MalformedEmailAddressException) as cm:
            extract_email_address_details('@@@').fail()
        self.assertEqual(
            'This is an invalid email address.',
            str(cm.exception)
        )


if __name__ == '__main__':
    unittest.main()

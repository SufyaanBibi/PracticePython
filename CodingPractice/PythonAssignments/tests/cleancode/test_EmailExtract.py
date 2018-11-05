import unittest
from CodingPractice.PythonAssignments.cleancode.EmailExtract \
    import EmailDetails, extract_email_address_details, MalformedEmailAddressException


class EmailExtractTests(unittest.TestCase):

    def test_00_is_id_valid(self):
        actual = extract_email_address_details( 'basil@5yp.com' )
        self.assertEqual('basil', actual._local_part)

    def test_01_can_extract_address(self):
        expected = EmailDetails('basil', '5yp.com')
        actual = extract_email_address_details( 'basil@5yp.com' )
        self.assertEqual(expected, actual)

    def test_02_valid_email_address(self):
        expected = EmailDetails('simple', 'example.com')
        actual = extract_email_address_details('simple@example.com')
        self.assertEqual(expected, actual)

    def test_03_valid_very_common_email_address(self):
        expected = EmailDetails('very.common', 'example.co.uk')
        actual = extract_email_address_details('very.common@example.co.uk')
        self.assertEqual(expected, actual)

    def test_04_valid_email_address_with_symbol(self):
        expected = EmailDetails('disposable.style.email.with+symbol', 'example.com')
        actual = extract_email_address_details('disposable.style.email.with+symbol@example.com')
        self.assertEqual(expected, actual)

    def test_05_valid_email_address_with_hyphen(self):
        expected = EmailDetails('other.email-with-hyphen', 'example.co.uk')
        actual = extract_email_address_details('other.email-with-hyphen@example.co.uk')
        self.assertEqual(expected, actual)

    def test_06_valid_email_address_fully_qualified_domain(self):
        expected = EmailDetails('fully-qualified-domain', 'example.com')
        actual = extract_email_address_details('fully-qualified-domain@example.com')
        self.assertEqual(expected, actual)

    def test_07_valid_email_address_with_tag_sorting(self):
        expected = EmailDetails('user.name+tag+sorting', 'example.com')
        actual = extract_email_address_details('user.name+tag+sorting@example.com')
        self.assertEqual(expected, actual)

    def test_08_valid_email_address_one_letter_local_part(self):
        expected = EmailDetails('x', 'example.com')
        actual = extract_email_address_details('x@example.com')
        self.assertEqual(expected, actual)

    def test_09_valid_email_address_strange_domain(self):
        expected = EmailDetails('example-indeed', 'strange-example.com')
        actual = extract_email_address_details('example-indeed@strange-example.com')
        self.assertEqual(expected, actual)

    def test_10_invalid_email_address_domain_name_no_TLD(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('admin@mailserver1')
        self.assertEqual('admin@mailserver1', e.exception.message)

    def test_11_valid_email_address_top_level_domain(self):
        expected = EmailDetails('example', 's.example')
        actual = extract_email_address_details('example@s.example')
        self.assertEqual(expected, actual)

    def test_12_valid_email_address_spaces(self):
        expected = EmailDetails('"  "', 'example.org')
        actual = extract_email_address_details('"  "@example.org')
        self.assertEqual(expected, actual)

    def test_13_exception_raised_for_malformed_email_address(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('BAD_EMAIL_ADDRESS')
        self.assertEqual('BAD_EMAIL_ADDRESS', e.exception.message)

    def test_14_missing_domain(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('sufi@')
        self.assertEqual('sufi@', e.exception.message)

    def test_15_missing_id(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('@5yp.com')
        self.assertEqual('@5yp.com', e.exception.message)

    def test_16_malformed_email(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('bbb@xyz,com@')
        self.assertEqual('bbb@xyz,com@', e.exception.message)

    def test_17_malformed_email(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('@@@')
        self.assertEqual('@@@', e.exception.message)

    def test_18_malformed_email(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('abc @ 123 .... abc .... com')
        self.assertEqual('abc @ 123 .... abc .... com', e.exception.message)

    def test_19_invalid_email_no_at_symbol(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('Abc.example.com')
        self.assertEqual('Abc.example.com', e.exception.message)

    def test_20_invalid_email_multiple_at_symbols(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('A@b@c@example.com')
        self.assertEqual('A@b@c@example.com', e.exception.message)

    def test_21_invalid_email_special_characters(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('a"b(c)d,e:f;g<h>i[j\k]l@example.com')
        self.assertEqual('a"b(c)d,e:f;g<h>i[j\k]l@example.com', e.exception.message)

    def test_22_invalid_email_quoted_strings_not_dot_separated(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('just"not"right@example.com')
        self.assertEqual('just"not"right@example.com', e.exception.message)

    def test_23_invalid_email_unquoted_invalid_characters(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('this is"not\allowed@example.com')
        self.assertEqual('this is"not\allowed@example.com', e.exception.message)

    def test_24_invalid_email_invalid_characters(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('this\ still\"not\\allowed@example.com')
        self.assertEqual('this\ still\"not\\allowed@example.com', e.exception.message)

    def test_25_invalid_email_local_part_exceeds_limit(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details(
                '1234567890123456789012345678901234567890123456789012345678901234+x@example.com'
            )
        self.assertEqual(
            '1234567890123456789012345678901234567890123456789012345678901234+x exceeds length constraint: 64 characters.',
            e.exception.message
        )

    def test_26_invalid_email_double_dot_before_at_symbol(self):
        with self.assertRaises(MalformedEmailAddressException) as e:
            extract_email_address_details('john..doe@example.com')
        self.assertEqual('john..doe@example.com', e.exception.message)


if __name__ == '__main__':
    unittest.main()

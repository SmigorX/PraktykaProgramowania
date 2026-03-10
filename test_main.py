import unittest
from main import add_numbers

class TestMain(unittest.TestCase):
    def test_add_with_two_values(self):
        self.values="1,2"
        self.expected=3
        self.assertEqual(add_numbers(self.values), self.expected)

    def test_add_with_one_value(self):
        self.values="1"
        self.expected=1
        self.assertEqual(add_numbers(self.values), self.expected)

    def test_add_with_zero_value(self):
        self.values=""
        self.expected=0
        self.assertEqual(add_numbers(self.values), self.expected)

    def test_add_with_multiple_values(self):
        self.values="1,2,3,4"
        self.expected=10
        self.assertEqual(add_numbers(self.values), self.expected)

    def test_add_with_value_error(self):
        self.values="abc"
        self.expected=ValueError
        with self.assertRaises(self.expected):
            add_numbers(self.values)

    def test_add_with_accept_newline_character_in_place_of_comma(self):
        self.values="10\n22"
        self.expected=32
        self.assertEqual(add_numbers(self.values), self.expected)

    def test_add_with_mix_of_comma_and_newlines(self):
        self.values="10\n2,5"
        self.expected=17
        self.assertEqual(add_numbers(self.values), self.expected)

    def test_add_with_value_error_on_missing_number_with_comma(self):
        self.values="1,"
        self.expected=ValueError
        with self.assertRaises(self.expected):
            add_numbers(self.values)

    def test_add_with_value_error_on_missing_number_with_newline(self):
        self.values="1\n"
        self.expected=ValueError
        with self.assertRaises(self.expected):
            add_numbers(self.values)
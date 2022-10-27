from unittest import TestCase
from fantasy5 import Fantasy5
from pprint import pprint


class TestFantasy5(TestCase):
    def test_generate_random_number(self) -> None:
        frequency_list = ['3', '3', '3', '3', '3', '3', '3', '3', '3', '2']
        f = Fantasy5()
        value = '3'  # unique value
        self.assertNotEqual(value, 3, "String '3' is not equal to Number 3")
        f.winning_number.add(int(value))
        self.assertTrue(int(value) in f.winning_number, "3 is winning number")
        pprint(f.winning_number)

        f.generate_random_number(frequency_list)
        self.assertTrue(len(f.winning_number) == 2, "Should add 2 to winning number eventually")
        pprint(f.winning_number)

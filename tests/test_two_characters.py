from algorithm_codes.two_characters import alternate
import unittest

class AlternateTest(unittest.TestCase):
    def test_two_characters_case1(self):
        s = "beabeefeab"
        result = alternate(s)
        self.assertEqual(result)
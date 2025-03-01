from algorithm_codes.two_characters import alternate
import unittest

class AlternateTest(unittest.TestCase):
    def test_two_characters_case1(self):
        s = "beabeefeab"
        result = alternate(s)
        self.assertEqual(result)

    def test_two_characters_case2(self):
        s = "ababab"
        result = alternate(s)
        self.assertEqual(result)

    def test_two_characters_case3(self):
        s = "aaaa"
        result = alternate(s)
        self.assertEqual(result)

    def test_two_characters_case4(self):
        s = "abcabcabc"
        result = alternate(s)
        self.assertEqual(result)

    def test_two_characters_case5(self):
        s = "xyxyxyxy"
        result = alternate(s)
        self.assertEqual(result)

    def test_two_characters_case6(self):
        s = "abcdef"
        result = alternate(s)
        self.assertEqual(result)

    def test_two_characters_case7(self):
        s = "aaaabbbb"
        result = alternate(s)
        self.assertEqual(result)

    def test_two_characters_case8(self):
        s = "aabbbccccd"
        result = alternate(s)
        self.assertEqual(result)

    def test_two_characters_case9(self):
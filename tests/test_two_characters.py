from algorithm_codes.two_characters import alternate
import unittest

class AlternateTest(unittest.TestCase):
    def test_two_characters_case1(self):
        s = "beabeefeab"
        expected_output = 5
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case2(self):
        s = "ababab"
        expected_output = 6 
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case3(self):
        s = "aaaa"
        expected_output = 0
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case4(self):
        s = "abcabcabc"
        expected_output = 6 
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case5(self):
        s = "xyxyxyxy"
        expected_output = 8
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case6(self):
        s = "abcdef"
        expected_output = 2 
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case7(self):
        s = "aaaabbbb"
        expected_output = 0
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case8(self):
        s = "aabbbccccd"
        expected_output = 2 
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case9(self):
        s = "ab"
        expected_output = 2
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case10(self):
        s = "xxyyzz"
        expected_output = 2 
        result = alternate(s)
        self.assertEqual(result, expected_output)

    def test_two_characters_case11(self):

if __name__ == '__main__':
    unittest.main()
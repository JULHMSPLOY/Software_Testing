from algorithm_codes.funny_string import funnyString
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_funny_string_case_1(self):
        s = "acxz"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_2(self):
        s = "bcxz"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_3(self):
        s = "a"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)
    
    def test_funny_string_case_4(self):
        s = "abccba"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_5(self):
        s = "abcd"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_6(self):
        s = "abab"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_7(self):
        s = "z"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)
        
    def test_funny_string_case_8(self):
        s = "aa"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_9(self):
        s = "az"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_10(self):
        s = "aba"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_11(self):
        s = "racecar"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_12(self):
        s = "abcdefgh"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_13(self):
        s = "hgfedcba"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_14(self):
        s = "aaaaaa"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_15(self):
        s = "12321"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_16(self):
        s = "a1b2b1a"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)
    
    def test_funny_string_case_17(self):
        s = "abcdabcd"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_18(self):
        s = "abc#cba"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_19(self):
        s = "a1b2b1a"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_20(self):
        s = "AbcCba"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_21(self):
        s = "abc cba"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_22(self):
        s = "abc@cba"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_23(self):
        s = "ab" * 50
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)
    
    def test_funny_string_case_24(self):
        s = "a" * 10000
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_25(self):
        s = "ab"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_26(self):
        s = "abcba"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_27(self):
        s = " abba"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_28(self):
        s = "abba "
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_29(self):
        s = "a b a"
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_30(self):
        s = "AbBa"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_31(self):
        s = "@#^&*"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_32(self):
        s = "abcabcabcabc"
        expected_output = "Not Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_33(self):
        s = "ab" * 5000
        expected_output = "Funny"
        encrypted = funnyString(s)
        self.assertEqual(encrypted, expected_output)

    def test_funny_string_case_34(self):
        q = "2"
        expected_output = "Funny"
        encrypted = funnyString(q)
        self.assertEqual(encrypted, expected_output)

    if __name__ == '__main__':
        unittest.main()
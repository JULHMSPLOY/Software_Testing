from algorithm_codes.funny_string import funnyString
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_funny_string_case_1(self):
        s = "acxz"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_2(self):
        s = "bcxz"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_3(self):
        s = "a"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)
    
    def test_funny_string_case_4(self):
        s = "abccba"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_5(self):
        s = "abcd"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_6(self):
        s = "abab"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_7(self):
        s = "z"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)
        
    def test_funny_string_case_8(self):
        s = "aa"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_9(self):
        s = "az"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_10(self):
        s = "aba"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_11(self):
        s = "racecar"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_12(self):
        s = "abcdefgh"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_13(self):
        s = "hgfedcba"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_14(self):
        s = "aaaaaa"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_15(self):
        s = "12321"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_16(self):
        s = "a1b2b1a"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)
    
    def test_funny_string_case_17(self):
        s = "abcdabcd"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_18(self):
        s = "abc#cba"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_19(self):
        s = "a1b2b1a"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_20(self):
        s = "AbcCba"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_21(self):
        s = "abc cba"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_22(self):
        s = "abc@cba"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_23(self):
        s = "ab" * 50
        encrypted = funnyString(s)
        self.assertEqual(encrypted)
    
    def test_funny_string_case_24(self):
        s = "a" * 10000
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_25(self):
        s = "ab"
        encrypted = funnyString(s)
        self.assertEqual(encrypted)

    def test_funny_string_case_26(self):
        self.assertEqual(funnyString("abcba"), "Not Funny")

    def test_funny_string_case_27(self):
        self.assertEqual(funnyString(" abba"), "Not Funny")

    def test_funny_string_case_28(self):
        self.assertEqual(funnyString("abba "), "Not Funny")

    def test_funny_string_case_29(self):
        self.assertEqual(funnyString("a b a"), "Not Funny")

    def test_funny_string_case_30(self):
        self.assertEqual(funnyString("AbBa"), "Not Funny")

    def test_funny_string_case_31(self):
        self.assertEqual(funnyString("@#^&*"), "Not Funny")

    def test_funny_string_case_32(self):
        self.assertEqual(funnyString("abcabcabcabc"), "Not Funny")

    def test_funny_string_case_33(self):
        self.assertEqual(funnyString("ab" * 5000), "Not Funny")

    def test_funny_string_case_34(self):
        self.assertEqual(funnyString(""), "Funny")

    if __name__ == '__main__':
        unittest.main()
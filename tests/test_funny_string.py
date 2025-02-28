from algorithm_codes.funny_string import funnyString
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_funny_string_case_1(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_funny_string_case_2(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_funny_string_case_3(self):
        self.assertEqual(funnyString("a"), "Funny")
    
    def test_funny_string_case_4(self):
        self.assertEqual(funnyString("abccba"), "Funny")

    def test_funny_string_case_5(self):
        self.assertEqual(funnyString("abcd"), "Not Funny")

    def test_funny_string_case_6(self):
        self.assertEqual(funnyString("abab"), "Not Funny")

    def test_funny_string_case_7(self):
        self.assertEqual(funnyString("z"), "Funny")
        
    def test_funny_string_case_8(self):
        self.assertEqual(funnyString("aa"), "Funny")

    def test_funny_string_case_9(self):
        self.assertEqual(funnyString("az"), "Not Funny")

    def test_funny_string_case_10(self):
        self.assertEqual(funnyString("aba"), "Funny")

    def test_funny_string_case_11(self):
        self.assertEqual(funnyString("racecar"), "Funny")

    def test_funny_string_case_12(self):
        self.assertEqual(funnyString("abcdefgh"), "Not Funny")

    def test_funny_string_case_13(self):
        self.assertEqual(funnyString("hgfedcba"), "Not Funny")

    def test_funny_string_case_14(self):
        self.assertEqual(funnyString("aaaaaa"), "Funny")

    def test_funny_string_case_15(self):
        self.assertEqual(funnyString("12321"), "Funny")

    def test_funny_string_case_16(self):
        self.assertEqual(funnyString("a1b2b1a"), "Funny")
    
    def test_funny_string_case_17(self):
        self.assertEqual(funnyString("abcdabcd"), "Not Funny")

    def test_funny_string_case_18(self):
        self.assertEqual(funnyString("abc#cba"), "Not Funny")

    def test_funny_string_case_19(self):
        self.assertEqual(funnyString("a1b2b1a"), "Funny")

    def test_funny_string_case_20(self):
        self.assertEqual(funnyString("AbcCba"), "Funny")

    def test_funny_string_case_21(self):
        self.assertEqual(funnyString("abc cba"), "Funny")

    def test_funny_string_case_22(self):
        self.assertEqual(funnyString("abc@cba"), "Not Funny")

    def test_funny_string_case_23(self):
        self.assertEqual(funnyString("ab" * 50), "Not Funny")
    
    def test_funny_string_case_24(self):
        self.assertEqual(funnyString("a" * 10000), "Funny")

    def test_funny_string_case_25(self):
        self.assertEqual(funnyString("ab"), "Not Funny")

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

    if __name__ == '__main__':
        unittest.main()
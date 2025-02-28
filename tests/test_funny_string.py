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

    if __name__ == '__main__':
        unittest.main()
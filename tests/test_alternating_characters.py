from algorithm_codes.alternating_characters import alternatingCharacters
import unittest

class AlternatingCharactersTest(unittest.TestCase):
    def test_alternating_characters_case1(self):
        s = "AAAA"
        expected_output = 3
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case2(self):
        s = "BBBBB"
        expected_output = 4
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case3(self):
        s = "ABABABAB"
        expected_output = 0
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)
    
    def test_alternating_characters_case4(self):
        s = "BABABA"
        expected_output = 0
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case5(self):
        s = "AAABBB"
        expected_output = 4
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case6(self):
        s = "A"
        expected_output = 0
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case7(self):
        s = "BBBBBBBBB"
        expected_output = 8
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case8(self):
        s = "ABABABABABABABABABAB"
        expected_output = 0
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case9(self):
        s = "AAAAAAAAAA"
        expected_output = 9
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case10(self):
        s = ""
        expected_output = 0
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case11(self):
        s = "AABBABBAA"
        expected_output = 4
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case12(self):
        s = "ABABBAB"
        expected_output = 2
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case13(self):
        s = "ABBAABBBAA"
        expected_output = 6
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case14(self):
        s = "A" * 100000
        expected_output = 99999
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case15(self):
        s = "AB" * 50000
        expected_output = 0
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case16(self):
        s = "ABBABBABBABB"
        expected_output = 4
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case17(self):
        s = "ABBAAB"
        expected_output = 3
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case18(self):
        s = "ABABAAA"
        expected_output = 2
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case19(self):
        s = "BAAABABABBABAA"
        expected_output = 5
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case20(self):
        s = "ABABABBABABA"
        expected_output = 2
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case21(self):
        s = "B" * 50000 + "A" + "B" * 49999
        expected_output = 99998
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

    def test_alternating_characters_case22(self):
        s = "AB" * 49999 + "AA"
        expected_output = 1
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, expected_output)

if __name__ == '__main__':
    unittest.main()
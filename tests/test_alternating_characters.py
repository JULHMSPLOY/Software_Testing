from algorithm_codes.alternating_characters import alternatingCharacters
import unittest

class AlternatingCharactersTest(unittest.TestCase):
    def test_alternating_characters_case1(self):
        s = "AAAA"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case2(self):
        s = "BBBBB"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case3(self):
        s = "ABABABAB"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)
    
    def test_alternating_characters_case4(self):
        s = "BABABA"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case5(self):
        s = "AAABBB"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case6(self):
        s = "A"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case7(self):
        s = "BBBBBBBBB"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case8(self):
        s = "ABABABABABABABABABAB"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case9(self):
        s = "AAAAAAAAAA"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case10(self):
        s = ""
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted, 0)

    def test_alternating_characters_case11(self):
        s = "AABBABBAA"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case12(self):
        s = "ABABBAB"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case13(self):
        s = "ABBAABBBAA"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case14(self):
        s = "A" * 100000
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case15(self):
        s = "AB" * 50000
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case16(self):
        s = "ABBABBABBABB"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case17(self):
        s = "ABBAAB"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case18(self):
        s = "ABABAAA"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case19(self):
        s = "BAAABABABBABAA"
        encrypted = alternatingCharacters(s)
        self.assertEqual(encrypted)

    def test_alternating_characters_case20(self):
        self.assertEqual(alternatingCharacters("ABABABBABABA"), 2)

    def test_alternating_characters_case21(self):
        self.assertEqual(alternatingCharacters("B" * 50000 + "A" + "B" * 49999), 99998)

    def test_alternating_characters_case22(self):
        self.assertEqual(alternatingCharacters("AB" * 49999 + "AA"), 1)

if __name__ == '__main__':
    unittest.main()
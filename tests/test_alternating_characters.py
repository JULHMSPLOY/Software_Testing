from algorithm_codes.alternating_characters import alternatingCharacters
import unittest

class AlternatingCharactersTest(unittest.TestCase):
    def test_alternating_characters_case1(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_alternating_characters_case2(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_alternating_characters_case3(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
    
    def test_alternating_characters_case4(self):
        self.assertEqual(alternatingCharacters("BABABA"), 0)
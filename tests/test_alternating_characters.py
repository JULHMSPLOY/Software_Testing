from algorithm_codes.alternating_characters import alternatingCharacters
import unittest

class AlternatingCharactersTest(unittest.TestCase):
    def test_alternating_characters_case1(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_alternating_characters_case2(self):
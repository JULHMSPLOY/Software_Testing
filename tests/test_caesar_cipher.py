from algorithm_codes.caesar_cipher import caesarCipher
import unittest

class CaesarCipherTest(unittest.TestCase):
    def test_caesar_cipher_case1(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
    
    def test_caesar_cipher_case2(self):
        self.assertEqual(caesarCipher("abc-XYZ", 3), "def-ABC")
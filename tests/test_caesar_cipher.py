from algorithm_codes.caesar_cipher import caesarCipher
import unittest

class CaesarCipherTest(unittest.TestCase):
    def test_caesar_cipher_case1(self):
        s = "middle-Outz"
        k = 2
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)
    
    def test_caesar_cipher_case2(self):
        s = "abcdef"
        k = 3
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)

    def test_caesar_cipher_case3(self):
        s = "abcXYZ"
        k = 5
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)

    def test_caesar_cipher_case4(self):
        s = "z"
        k = 1
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)
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

    def test_caesar_cipher_case5(self):
        s = "a-b-CdEf!"
        k = 4
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)

    def test_caesar_cipher_case6(self):
        s = "hello"
        k = 26
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)

    def test_caesar_cipher_case7(self):
        s = "hello-world"
        k = 0
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)

    def test_caesar_cipher_case8(self):
        s = "aZy-x"
        k = 25
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)

    def test_caesar_cipher_case9(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        k = 13
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)

    def test_caesar_cipher_case10(self):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        k = 5
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted)
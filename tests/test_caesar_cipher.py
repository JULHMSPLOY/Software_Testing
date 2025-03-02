from algorithm_codes.caesar_cipher import caesarCipher
import unittest

class CaesarCipherTest(unittest.TestCase):
    def test_caesar_cipher_case1(self):
        s = "middle-Outz"
        k = 2
        expected_output = "okffng-Qwvb"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)
    
    def test_caesar_cipher_case2(self):
        s = "abcdef"
        k = 3
        expected_output = "defghi"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case3(self):
        s = "abcXYZ"
        k = 5
        expected_output = "fghCDE"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case4(self):
        s = "z"
        k = 1
        expected_output = "a"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case5(self):
        s = "a-b-CdEf!"
        k = 4
        expected_output = "e-f-GhIj!"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case6(self):
        s = "hello"
        k = 26
        expected_output = "hello"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case7(self):
        s = "hello-world"
        k = 0
        expected_output = "hello-world"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case8(self):
        s = "aZy-x"
        k = 25
        expected_output = "zYx-w"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case9(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        k = 13
        expected_output = "nopqrstuvwxyzabcdefghijklm"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case10(self):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        k = 5
        expected_output = "FGHIJKLMNOPQRSTUVWXYZABCDE"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case11(self):
        s = "abc"
        k = 30
        expected_output = "efg"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case12(self):
        s = "HelloWorld"
        k = 3
        expected_output = "KhoorZruog"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case13(self):
        s = "123!@#"
        k = 4
        expected_output = "123!@#"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

    def test_caesar_cipher_case14(self):
        s = "hello"
        k = -1
        expected_output = "gdkkn"
        encrypted = caesarCipher(s, k)
        self.assertEqual(encrypted, expected_output)

if __name__ == '__main__':
    unittest.main()
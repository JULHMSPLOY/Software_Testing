def caesarCipher(s, k):
    k = k % 26
    encrypted_text = []

    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
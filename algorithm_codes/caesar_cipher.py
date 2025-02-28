def caesarCipher(s, k):
    k = k % 26
    encrypted_text = []

    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
        elif 'A' <= char <= 'z':
            new_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
        else:
            new_char = char

        encrypted_text.append(new_char)
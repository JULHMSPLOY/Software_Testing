def caesarCipher(s, k):
    k = k % 26
    encrypted_text = []

    for char in s:
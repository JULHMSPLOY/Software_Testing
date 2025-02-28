def funnyString(s):
    reversed_s = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(reversed_s[i]) - ord(reversed_s[i - 1])):
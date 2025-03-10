def alternate(s):
    unique_chars = list(set(s))
    max_length = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]

            filtered_string = [c for c in s if c == char1 or c == char2]

            if all(filtered_string[k] != filtered_string[k + 1] for k in range(len(filtered_string) - 1)):
                max_length = max(max_length, len(filtered_string))

    return max_length
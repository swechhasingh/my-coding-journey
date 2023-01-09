# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# time complexity: O(N) and space complexity: O(N)
def find_longest_substring_with_k_distinct_chars(inp_str: str, K: int):
    char_count = dict()
    start = 0
    longest_substring_len = 0
    sub_str = None
    for end in range(len(inp_str)):
        # if len(char_count) <= K:
        char_count[inp_str[end]] = char_count.get(inp_str[end], 0) + 1
        # shrink window
        if len(char_count) > K:
            longest_substring_len = max(longest_substring_len, end - start)
            if longest_substring_len == (end - start):
                sub_str = inp_str[start:end]
        while len(char_count) > K:
            start_char = inp_str[start]
            char_count[start_char] -= 1
            if char_count[start_char] == 0:
                char_count.pop(start_char)
            start += 1
    return longest_substring_len, sub_str


if __name__ == "__main__":
    print(
        f"Length of the longest substring: {find_longest_substring_with_k_distinct_chars('araaci', 2)}"
    )
    print(
        f"Length of the longest substring: {find_longest_substring_with_k_distinct_chars('araaci', 1)}"
    )

    print(
        f"Length of the longest substring: {find_longest_substring_with_k_distinct_chars('cbbebi', 3)}"
    )

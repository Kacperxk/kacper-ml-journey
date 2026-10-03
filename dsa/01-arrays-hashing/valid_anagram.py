"""Valid Anagram — https://leetcode.com/problems/valid-anagram

Approach: making characters as keys and values how many times they appeared, then comparing two dictionaries
Time: O(n) — n iterations over O(1)
Space: O(1) — 26 alphabet characters
"""

def count_chars(text: str) -> dict[str, int]:
    counts = {}
    for ch in text:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return count_chars(s) == count_chars(t)


if __name__ == "__main__":
    assert is_anagram("cat", "tac")
    assert is_anagram("", "")
    assert not is_anagram("cat", "cad")
    assert not is_anagram("a", "ab")
    assert not is_anagram("aab", "abb")
    print("all tests passed")
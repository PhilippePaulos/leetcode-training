import pytest


# Return the index of the first occurrence of needle in haystack, or -1 if absent.
# O(nxm)
def str_str(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    for i in range(n - m +1):
        if haystack[i:i+m] == needle:
            return i
    return -1


@pytest.mark.parametrize(
    ("haystack", "needle", "expected"),
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("mississippi", "issip", 4),
        ("abc", "abc", 0),
        ("abc", "abcd", -1),
        ("a", "a", 0),
    ],
)
def test_str_str(haystack, needle, expected):
    assert str_str(haystack, needle) == expected

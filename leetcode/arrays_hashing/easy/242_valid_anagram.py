from collections import defaultdict

import pytest


# defaultdict counting - Time: O(n), Space: O(1) (at most 26 keys)
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    for c in t:
        counts[c] -= 1
        if counts[c] < 0:
            return False
    return True

# Plain dict with .get() - Time: O(n), Space: O(1) (at most 26 keys)
def is_anagram_standard(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in t:
        counts[c] = counts.get(c, 0) - 1
        if counts[c] < 0:
            return False
    return True

# Fixed 26-slot count arrays - Time: O(n), Space: O(1)
def is_anagram_optimized(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = [0] * 26
    for c1, c2 in zip(s, t):
        counts[ord(c1) - ord('a')] += 1
        counts[ord(c2) - ord('a')] -= 1
    return all(c == 0 for c in counts)


@pytest.mark.parametrize("solve", [is_anagram, is_anagram_standard, is_anagram_optimized])
@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("racecar", "carrace", True),
        ("a", "ab", False),
        ("", "", True),
    ],
)
def test_is_anagram(solve, s, t, expected):
    assert solve(s, t) is expected
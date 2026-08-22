from collections import defaultdict


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

def is_anagram_optimized(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = [0] * 26
    for c1, c2 in zip(s, t):
        counts[ord(c1) - ord('a')] += 1
        counts[ord(c2) - ord('a')] -= 1
    return all(c == 0 for c in counts)

if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    print(is_anagram_optimized(s, t))
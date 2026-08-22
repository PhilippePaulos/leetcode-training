from collections import defaultdict

# Input: strs =
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

def group_anagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        res["".join(sorted(s))].append(s)
    return list(res.values())

if __name__ == "__main__":
    result = group_anagrams(["act","pots","tops","cat","stop","hat"])
    print(result)

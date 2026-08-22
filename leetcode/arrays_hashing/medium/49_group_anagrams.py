from collections import defaultdict

import pytest

# Sorted string as key - Time: O(n * k log k), Space: O(n * k), k = max word length
def group_anagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        res["".join(sorted(s))].append(s)
    return list(res.values())


@pytest.mark.parametrize(
    ("strs", "expected"),
    [
        (
            ["act", "pots", "tops", "cat", "stop", "hat"],
            [["act", "cat"], ["hat"], ["pots", "stop", "tops"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams(strs, expected):
    def normalize(groups):
        return sorted(sorted(group) for group in groups)

    assert normalize(group_anagrams(strs)) == normalize(expected)

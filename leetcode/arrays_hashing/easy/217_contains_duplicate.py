from typing import List

import pytest


# Hash set of seen values - Time: O(n), Space: O(n)
def has_duplicate(nums: List[int]) -> bool:
    viewed = set()
    for num in nums:
        if num in viewed:
            return True
        viewed.add(num)
    return False


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([], False),
        ([7], False),
    ],
)
def test_has_duplicate(nums, expected):
    assert has_duplicate(nums) is expected

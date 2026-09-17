import pytest


# O(n) complexity & space
def longest_consecutive(nums: list[int]) -> int:
    values = set(nums)
    longest = 0
    for x in values:
        if x-1 not in values:
            end = x
            while end in values:
                end+=1
            longest = max(end - x, longest)

    return longest


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([], 0),
    ],
)
def test_longest_consecutive(nums, expected):
    assert longest_consecutive(nums) == expected
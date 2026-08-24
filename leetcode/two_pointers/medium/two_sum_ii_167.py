import pytest


# LeetCode 167 - Two Sum II (Input Array Is Sorted)
# numbers is sorted in non-decreasing order (1-indexed).
# Return [i, j] with i < j and numbers[i-1] + numbers[j-1] == target.
# Exactly one solution exists, the same element cannot be used twice.
# Constraint: O(1) extra space.
def two_sum(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum == target:
            return [i + 1, j+1]
        if numbers[i] + numbers[j] > target:
            j -=1
            continue
        if numbers[i] + numbers[j] < target:
            i += 1
            continue
    return []

@pytest.mark.parametrize(
    ("numbers", "target", "expected"),
    [
        # ([2, 3, 11, 15], 18, [2, 4]),
        # ([2, 3, 4], 6, [1, 3]),
        # ([-1, 0], -1, [1, 2]),
        # ([1, 2, 3, 4], 3, [1, 2]),
        # ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        # ([5, 25, 75], 100, [2, 3]),
        ([-3, -1, 0, 2, 4], 1, [1, 5]),
        # ([1, 1], 2, [1, 2]),
    ],
)
def test_two_sum(numbers, target, expected):
    assert two_sum(numbers, target) == expected

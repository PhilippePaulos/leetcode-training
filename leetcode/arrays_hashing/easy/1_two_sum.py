import pytest


# Brute force: try every pair - Time: O(n^2), Space: O(1)
def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# One-pass hash map - Time: O(n), Space: O(n)
def two_sum_optimized(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        c = target - num
        if c in seen:
            return [seen[c], i]
        seen[num] = i
    return []


@pytest.mark.parametrize("solve", [two_sum, two_sum_optimized])
@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3], 100, []),
    ],
)
def test_two_sum(solve, nums, target, expected):
    assert solve(nums, target) == expected
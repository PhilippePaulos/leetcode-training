import pytest


class NumArray:
    def __init__(self, nums: list[int]):
        self.sums = [0] * (len(nums) + 1)
        prefix = 0
        for i in range(1, len(nums) + 1):
            prefix += nums[i-1]
            self.sums[i] = prefix

    def sum_range(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (0, 2, 1),
        (2, 5, -1),
        (0, 5, -3),
    ],
)
def test_sum_range(left, right, expected):
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    assert num_array.sum_range(left, right) == expected

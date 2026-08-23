import pytest


# Prefix & suffix products - Time: O(n), Space: O(1) (output array excluded)
# Two passes: answer[i] = product of everything before i, then multiply by product of everything after i
def product_of_array(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

@pytest.mark.parametrize(
    "nums",
    [
        ([1, 2, 4, 6]),
    ],
)
def test_top_k_frequent(nums):
    assert product_of_array(nums) == [48,24,12,8]

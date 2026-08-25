import pytest


# O(n2) complexity, O(1) space
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # optimization
        if nums[i] > 0:
            break

        j, k = i+1, len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j+=1
            elif total > 0:
                k-=1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j+=1
                while j <k and nums[j] == nums[j-1]:
                    j +=1
                k -= 1
    return res


def normalize(triplets: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(t) for t in triplets)


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([1, 2, -2, -1], []),
        ([3, -2, 1, 0], []),
        ([-1, 0, 1], [[-1, 0, 1]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
    ],
)
def test_three_sum(nums, expected):
    assert normalize(three_sum(nums)) == normalize(expected)

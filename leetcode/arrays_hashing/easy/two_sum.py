def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_optimized(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        c = target - num
        if c in seen:
            return [seen[c], i]
        seen[num] = i
    return []
import heapq
from collections import Counter

import pytest


# Sort all by frequency - Time: O(n log n), Space: O(n)
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return [num for num, _ in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k]]

# Heap via nlargest - Time: O(n log k), Space: O(n)
def top_k_frequent_2(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return heapq.nlargest(k, counts, key=counts.get)

# Bucket sort - Time: O(n), Space: O(n)
# Frequencies are in a known interval [1, n]: use them as list indices instead of comparing them
def top_k_frequent_optimized(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


@pytest.mark.parametrize("solve", [top_k_frequent, top_k_frequent_2, top_k_frequent_optimized])
@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 5, 5, 6], 2, {4, 5}),
    ],
)
def test_top_k_frequent(solve, nums, k, expected):
    result = solve(nums, k)
    assert len(result) == k
    assert set(result) == expected
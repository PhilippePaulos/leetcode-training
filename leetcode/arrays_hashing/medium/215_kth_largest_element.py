import heapq

import pytest


# Min-heap of size k - Time: O(n log k), Space: O(k)
def kth_largest_element(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif heap[0] < num:
            heapq.heappushpop(heap, num)
    return heap[0]

# Counting over bounded range [-10^4, 10^4] - Time: O(n + V), Space: O(V), V = value range
def kth_largest_elements_buckets(nums: list[int], k: int) -> int:
    offset = 10_000
    counts = [0] * (2 * offset + 1)
    for num in nums:
        counts[num + offset] += 1

    remaining = k
    for i in reversed(range(len(counts))):
        remaining -= counts[i]
        if remaining <= 0:
            return i - offset
    return 0


@pytest.mark.parametrize("solve", [kth_largest_element, kth_largest_elements_buckets])
@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([-5, -2, -10], 2, -5),
    ],
)
def test_kth_largest(solve, nums, k, expected):
    assert solve(nums, k) == expected
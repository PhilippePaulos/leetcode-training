import heapq


def kth_largest_element(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif heap[0] < num:
            heapq.heappushpop(heap, num)
    return heap[0]

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

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(kth_largest_elements_buckets(nums, k))
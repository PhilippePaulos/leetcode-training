import heapq
from collections import Counter


# O(n log n)
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return [num for num, _ in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k]]

# O(n log k)
def top_k_frequent_2(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return heapq.nlargest(k, counts, key=counts.get)

# O(n) #
# Uses bucket sorting
# Values to sort are in a known interval, use them as a position of a list instead of comparing them
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


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print(top_k_frequent_2(nums, k))
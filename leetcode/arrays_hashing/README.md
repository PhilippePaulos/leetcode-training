# Patterns - Arrays & Hashing

## 1. One-pass hash map

**When**: you're looking for an element's "partner" (complement, duplicate, anagram). Remember what you've already seen to avoid re-scanning. Trades memory for time: O(n²) → O(n).

**Skeleton**:

```python
seen = {}  # value already seen -> index
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

**Pitfall**: look up *before* inserting, otherwise an element can match itself.

**Key = signature variant**: to group anagrams, the dict key is `"".join(sorted(s))`. Pick the key that makes equal what you want to group together.

**Tools**: `dict.get(k, 0)`, `setdefault`, `defaultdict(list)`, `Counter`.

**Problems**: Two Sum (1), Valid Anagram (242), Group Anagrams (49).

---

## 2. Buckets / counting sort

**When**: you want to rank or select by **small bounded integers** (frequencies between 1 and n, values in [-10⁴, 10⁴]). Use the value as an *index* instead of comparing it → no sorting, O(n + V).

**Skeleton** (top k by frequency):

```python
counts = Counter(nums)
buckets = [[] for _ in range(len(nums) + 1)]  # buckets[f] = elements with frequency f
for num, freq in counts.items():
    buckets[freq].append(num)
result = []
for freq in reversed(range(len(buckets))):
    for num in buckets[freq]:
        result.append(num)
        if len(result) == k:
            return result
```

**Pitfalls**:

- With negative values: `index = value + OFFSET`.

**Limit**: if the value range is huge (10⁹), not feasible → heap.

**Problems**: Top K Frequent Elements (347), Sort Characters By Frequency (451), Kth Largest (215, buckets version).

---

## 3. Heap for top-k

**When**: select the k largest/smallest without sorting everything, **unbounded** values. O(n log k) instead of O(n log n).

**Core idea**: a heap only answers "what's the smallest?" but in O(1). Choose what you keep inside it so that the smallest *is* the answer. For the k largest → min-heap of size k, `heap[0]` = the k-th largest.

**Skeleton**:

```python
heap = []
for num in nums:
    if len(heap) < k:
        heapq.heappush(heap, num)
    elif num > heap[0]:
        heapq.heappushpop(heap, num)
return heap[0]
```

**API**: `heappush`, `heappop`, `heappushpop`, `heapify`, `heap[0]`. Min-heap only; for a max-heap, push `-x`. Shortcut: `heapq.nlargest(k, iterable, key=...)`.

**Problems**: Kth Largest Element (215), Top K Frequent (347, heap version).

---

## Choosing between 2 and 3

| What you're ranking | Tool | Complexity |
| --- | --- | --- |
| Small bounded integers | buckets | O(n + V) |
| Arbitrary values | heap of size k | O(n log k) |
| k = everything, or readability | `sorted` / `most_common` | O(n log n) |

In an interview: give the `sorted` version first, then explain how to optimize and why.

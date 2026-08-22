# leetcode
Place where I practice my algorithm skills

Target:
https://leetcode.com/problems/minimum-cost-to-merge-stones/description/

---

## Run

Tests live directly in each solution module ([uv](https://docs.astral.sh/uv/) manages the venv and dependencies):

```bash
uv sync                                 # once: create the venv and install pytest
uv run pytest                           # run every solution's tests
uv run pytest leetcode/arrays_hashing   # run a single topic
```

## Solutions

### Arrays & Hashing

| # | Problem | Difficulty | Pattern | Solution |
| --- | --- | --- | --- | --- |
| 1 | Two Sum | Easy | One-pass hash map | [1_two_sum.py](leetcode/arrays_hashing/easy/1_two_sum.py) |
| 217 | Contains Duplicate | Easy | Hash set | [217_contains_duplicate.py](leetcode/arrays_hashing/easy/217_contains_duplicate.py) |
| 242 | Valid Anagram | Easy | Character counting | [242_valid_anagram.py](leetcode/arrays_hashing/easy/242_valid_anagram.py) |
| 49 | Group Anagrams | Medium | Key = signature | [49_group_anagrams.py](leetcode/arrays_hashing/medium/49_group_anagrams.py) |
| 215 | Kth Largest Element | Medium | Heap of size k | [215_kth_largest_element.py](leetcode/arrays_hashing/medium/215_kth_largest_element.py) |
| 347 | Top K Frequent Elements | Medium | Buckets | [347_top_k_frequent_elements.py](leetcode/arrays_hashing/medium/347_top_k_frequent_elements.py) |
| 451 | Sort Characters By Frequency | Medium | Buckets | [451_sort_characters_by_frequency.py](leetcode/arrays_hashing/medium/451_sort_characters_by_frequency.py) |

### Trees & Graphs

| # | Problem | Difficulty | Pattern | Solution |
| --- | --- | --- | --- | --- |
| 101 | Symmetric Tree | Easy | Mirror DFS | [101_symmetric_tree.py](leetcode/graphs/easy/101_symmetric_tree.py) |
| 104 | Maximum Depth of Binary Tree | Easy | Recursive DFS | [104_max_depth.py](leetcode/graphs/easy/104_max_depth.py) |
| 110 | Balanced Binary Tree | Easy | Bottom-up DFS | [110_balanced_binary_tree.py](leetcode/graphs/easy/110_balanced_binary_tree.py) |
| 543 | Diameter of Binary Tree | Easy | Bottom-up DFS | [543_diameter_binary_tree.py](leetcode/graphs/easy/543_diameter_binary_tree.py) |

---

## Pattern notes

- [Arrays & Hashing](leetcode/arrays_hashing/README.md) - one-pass hash map, buckets / counting sort, top-k heap
- Trees & Graphs - coming soon

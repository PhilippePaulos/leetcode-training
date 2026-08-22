from collections import Counter


# Bucket sort by frequency - Time: O(n), Space: O(n)
def sort_characters_by_frequency(s: str) -> str:
    counts = Counter(s)
    buckets = [[] for _ in range(len(s) + 1)]
    for char, freq in counts.items():
        buckets[freq].append(char)

    parts = []
    for freq in range(len(buckets) - 1, 0, -1):
        for char in buckets[freq]:
            parts.append(char * freq)
    return "".join(parts)


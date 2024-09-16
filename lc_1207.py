# 1207. Unique Number of Occurrences


from typing import List
from collections import defaultdict, Counter


class Solution:
    # My Solution
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = defaultdict(int)
        for num in arr:
            count_map[num] += 1

        unique_counts = set()
        for count in count_map.values():
            if count in unique_counts:
                return False
            unique_counts.add(count)

        return True

    # Easy Solution
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_count = Counter(arr)
        counts = set(occurrence_count.values())
        return len(counts) == len(occurrence_count.values())


result = Solution()
arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
output = result.uniqueOccurrences(arr)
print(f"Output: {output}")
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

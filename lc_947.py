# 947. Most Stones Removed with Same Row or Column


from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_map = defaultdict(int)
        col_map = defaultdict(int)
        removed_stones = 0
        for row, col in stones:
            row_map[row] += 1
            col_map[col] += 1

        while len(stones) > 1:
            (row, col) = stones.pop()
            if row_map[row] > 1 or col_map[col] > 1:
                removed_stones += 1

        return removed_stones


result = Solution()
stones = [[3, 2], [3, 1], [4, 4], [1, 1], [0, 2], [4, 0]]
output = result.removeStones(stones)
print(f"Output: {output}")
expected = 4
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

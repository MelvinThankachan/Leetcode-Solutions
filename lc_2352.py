# 2352. Equal Row and Column Pairs


from typing import List
from collections import defaultdict, Counter


class Solution:
    # My Solution
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count_map = Counter([tuple(row) for row in grid])
        pairs = 0

        for col in range(n):
            column = tuple(grid[row][col] for row in range(n))
            pairs += count_map[column]

        return pairs

    # Advanced Solution
    def equalPairs(self, grid: List[List[int]]) -> int:
        count_map = Counter([tuple(row) for row in grid])
        pairs = 0
        for col in zip(*grid):
            pairs += count_map[tuple(col)]
        return pairs


result = Solution()
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
output = result.equalPairs(grid)
print(f"Output: {output}")
expected = 3
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

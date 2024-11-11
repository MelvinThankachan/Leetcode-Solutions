# 1466. Reorder Routes to Make All Paths Lead to the City Zero


from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        pass


result = Solution()
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
output = result.minReorder(n, connections)
print(f"Output: {output}")
expected = 3
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

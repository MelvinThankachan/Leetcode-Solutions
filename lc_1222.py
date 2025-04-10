from typing import List
from utils import are_equal_arrays


class Solution:
    def queensAttackTheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        directions = [
            [1, 0],  # right
            [-1, 0],  # left
            [0, 1],  # down
            [0, -1],  # up
            [1, 1],  # right down
            [1, -1],  # right up
            [-1, 1],  # left down
            [-1, -1],  # left up
        ]

        result = []

        for direction in directions:
            i = king[0]
            j = king[1]

            while 0 <= i < 8 and 0 <= j < 8:
                if [i, j] in queens:
                    result.append([i, j])
                    break
                i += direction[0]
                j += direction[1]

        return result


result = Solution()
queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
king = [0, 0]
output = result.queensAttackTheKing(queens, king)
print(f"Output: {output}")
expected = [[0, 1], [1, 0], [3, 3]]
if are_equal_arrays(output, expected):
    print("Test passed successfully!")
else:
    print("Test failed!")

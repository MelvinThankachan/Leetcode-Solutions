from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        prev_row = points[0]

        for row in range(1, ROWS):
            left_points = [0] * COLS
            right_points = [0] * COLS

            left_points[0] = prev_row[0]
            for col in range(1, COLS):
                left_points[col] = max(prev_row[col], left_points[col - 1] - 1)

            right_points[COLS - 1] = prev_row[COLS - 1]
            for col in range(COLS - 2, -1, -1):
                right_points[col] = max(prev_row[col], right_points[col + 1] - 1)

            for col in range(COLS):
                points[row][col] += max(left_points[col], right_points[col])

            prev_row = points[row]

        return max(prev_row)


result = Solution()
points = [[5, 2, 1, 2], [2, 1, 5, 2], [5, 5, 5, 0]]
output = result.maxPoints(points)
print(f"Output: {output}")
expected = 13
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


from typing import List


class Solution(object):
    # First Solution
    def maxArea(self, height):
        n = len(height)
        left = 0
        right = n - 1
        store = 0

        for i in range(n):
            if left == right:
                break

            left_height = height[left]
            right_height = height[right]

            min_height = min(left_height, right_height)
            water = min_height * abs(left - right)
            print(f"height: {height}")
            print(f"left: {left}, right: {right}")
            if water > store:
                store = water

            if right_height > left_height:
                left += 1
            else:
                right -= 1

        return store


    # Updated solution
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]
            water = 0
            length = right - left
            if left_height < right_height:
                water += left_height * length
                left += 1
            else:
                water += right_height * length
                right -= 1
            max_water = max(max_water, water)

        return max_water


result = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
output = result.maxArea(height)
print(f"Output: {output}")
expected = 49
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

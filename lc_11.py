class Solution(object):
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
            # print(left_height, right_height)
            # print(f"left - right: {abs(left - right)}")
            # print(f"min height: {min_height}")
            # print(f"water: {water}")
            if water > store:
                store = water

            if right_height > left_height:
                left += 1
            else:
                right -= 1
        
        return store


result = Solution()
height = [2,3,4,5,18,17,6]
output = result.maxArea(height)

print(output)

expected = 17

if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


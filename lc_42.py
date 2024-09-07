class Solution(object):
    def trap(self, height):
        n = len(height)
        left_top = [0] * n
        right_top = [0] * n
        trap = 0

        for i in range(1, n):
            left_top[i] = max(height[i - 1], left_top[i - 1])
            right_top[n - 1 - i] = max(height[n - i], right_top[n - i])
        
        for i in range(n):
            dip = min(left_top[i], right_top[i]) - height[i]
            if dip > 0:
                trap += dip

        return trap

result = Solution()
height = [4,2,0,3,2,5]
output = result.trap(height)
print(f"Output: {output}")
expected_output = 9
if output == expected_output:
    print("Test passed successfully!")
else:
    print("Test failed!")

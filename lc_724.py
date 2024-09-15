# 724. Find Pivot Index


from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1


result = Solution()
nums = [2, 1, -1]
output = result.pivotIndex(nums)
print(f"Output: {output}")
expected = 0
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

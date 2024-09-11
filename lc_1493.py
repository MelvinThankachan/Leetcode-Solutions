# 1493. Longest Subarray of 1's After Deleting One Element


from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = zeros = 0

        while right < n:
            if nums[right] == 0:
                zeros += 1
            if zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            right += 1

        return right - left - 1


result = Solution()
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
output = result.longestSubarray(nums)
print(f"Output: {output}")
expected = 5
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

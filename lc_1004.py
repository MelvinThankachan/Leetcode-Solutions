# 1004. Max Consecutive Ones III


from typing import List


class Solution:
    # My Solution
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zeros = max_ones = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ones = right + 1 - left 
            if ones > max_ones:
                max_ones = ones

        return max_ones
    
    # Another Solution
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        for right, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[left]
                left += 1

        return right - left + 1




result = Solution()
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
output = result.longestOnes(nums, k)
print(f"Output: {output}")
expected = 10
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

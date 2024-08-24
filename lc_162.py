# 162. Find Peak Element


class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        for i in range(1, n-1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i


result = Solution()
nums = [1,2,3,1]
output = result.findPeakElement(nums)
print(output)
expected = 2
if output == expected:
    print("Test passed successfully!")
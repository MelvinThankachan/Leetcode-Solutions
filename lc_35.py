# 35. Search Insert Position


# Linear Search
class Solution(object):
    def searchInsert(self, nums, target):
        index = 0
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif num < target:
                index += 1
            else:
                break
        return index


# Binary Search
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right)
            mid_element = nums[mid]
            if mid_element == target:
                return mid
            elif mid_element > target:
                right = mid - 1
            elif mid_element < target:
                left = mid + 1
        return left


result = Solution()
nums = [1, 3, 5, 6]
target = 3
output = result.searchInsert(nums, target)
print(f"Output: {output}")
expected_output = 1
if output == expected_output:
    print("Test passed successfully!")
else:
    print("Test failed!")

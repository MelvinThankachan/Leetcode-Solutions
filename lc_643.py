# 643. Maximum Average Subarray I


from typing import List


class Solution:
    # My Solution
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = left + k
        total = sum(nums[left : right - 1])
        n = len(nums)
        max_avg = float("-inf")
        prev_left = 0

        while right <= n:
            total = total - prev_left + nums[right - 1]
            avg = total / k
            max_avg = max(max_avg, avg)
            prev_left = nums[left]
            left += 1
            right += 1

        return max_avg

    # Better Solution
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k
        total = sum(nums[left:right])
        max_total = total

        while right < n:
            total = total - nums[left] + nums[right]
            max_total = max(max_total, total)
            left += 1
            right += 1

        return max_total / k


result = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
output = result.findMaxAverage(nums, k)
print(f"Output: {output}")
expected = 12.75000
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

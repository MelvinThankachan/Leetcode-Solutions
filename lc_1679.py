# 1679. Max Number of K-Sum Pairs


from typing import List
from collections import defaultdict


class Solution:
    # Memory Efficient
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total < k:
                left += 1
            elif total > k:
                right -= 1
            else:
                operations += 1
                left += 1
                right -= 1

        return operations

    # Time Efficient
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        num_map = defaultdict(int)

        for num in nums:
            need = k - num
            if num_map[need] > 0:
                operations += 1
                num_map[need] -= 1
            else:
                num_map[num] += 1

        return operations


result = Solution()
nums = [3, 1, 3, 4, 3]
k = 6
output = result.maxOperations(nums, k)
print(f"Output: {output}")
expected = 1
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

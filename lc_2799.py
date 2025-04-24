# 2799. Count Complete Subarrays in an Array


from typing import List
from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_count = len(set(nums))
        freq = defaultdict(int)
        left = 0
        count = 0
        distinct_in_window = 0
        n = len(nums)

        for right in range(n):
            freq[nums[right]] += 1
            if freq[nums[right]] == 1:
                distinct_in_window += 1

            while distinct_in_window == unique_count:
                count += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct_in_window -= 1
                left += 1

        return count


result = Solution()
nums = [1, 3, 1, 2, 2]
output = result.countCompleteSubarrays(nums)
print(f"Output: {output}")
expected = 4
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

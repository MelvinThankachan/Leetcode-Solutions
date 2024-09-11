# 485. Max Consecutive Ones


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for num in nums:
            count = count + 1 if num == 1 else 0
            if count > max_count:
                max_count = count

        return max_count


result = Solution()
nums = [1, 0, 1, 1, 0, 1]
output = result.findMaxConsecutiveOnes(nums)
print(f"Output: {output}")
expected = 2
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

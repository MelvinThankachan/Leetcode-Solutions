# 334. Increasing Triplet Subsequence


from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = third = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


result = Solution()
nums = [1, 5, 0, 4, 1, 3]
output = result.increasingTriplet(nums)
print(f"Output: {output}")
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

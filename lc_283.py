# 283. Move Zeroes


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = j = 0
        n = len(nums)

        while i < n:
            if nums[i] != 0 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[j] != 0:
                j += 1
            i += 1

        return nums


result = Solution()
nums = [0, 1, 2, 3, 5, 0, 7, 8, 0, 12]
output = result.moveZeroes(nums)
print(f"Output: {output}")
expected = [1, 2, 3, 5, 7, 8, 12, 0, 0, 0]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

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
nums = [
    45192,
    0,
    -659,
    -52359,
    -99225,
    -75991,
    0,
    -15155,
    27382,
    59818,
    0,
    -30645,
    -17025,
    81209,
    887,
    64648,
]
output = result.moveZeroes(nums)
print(f"Output: {output}")
expected = [
    45192,
    -659,
    -52359,
    -99225,
    -75991,
    -15155,
    27382,
    59818,
    -30645,
    -17025,
    81209,
    887,
    64648,
    0,
    0,
    0,
]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

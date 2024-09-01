from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MODULO = 10**9 + 7
        sums = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                sums.append(sum(nums[i:j]) % MODULO)
        sums.sort()
        return sum(sums[left - 1 : right]) % MODULO


result = Solution()
nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
output = result.rangeSum(nums, n, left, right)
print(f"Output: {output}")
expected = 13
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


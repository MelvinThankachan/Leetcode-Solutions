# 152. Maximum Product Sub-array


class Solution(object):
    def maxProduct(self, nums):
        result = nums[0]
        n = len(nums)
        for i in range(n):
            mul = nums[i]
            for j in range(i + 1, n):
                mul *= nums[j]
                if mul > result:
                    result = mul
        return result


result = Solution()
nums = [-2,0,-1]
output = result.maxProduct(nums)
print(f"Output: {output}")
expected = 0
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


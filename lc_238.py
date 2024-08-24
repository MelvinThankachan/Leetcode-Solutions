class Solution:
    def productExceptSelf(self, nums):
        len_nums = len(nums)
        pre_product = 1
        post_product = 1
        solution = [1] * len_nums

        for i in range(len_nums-1):
            pre_product *= nums[i]
            solution[i+1] *= pre_product
            post_product *= nums[len_nums - i - 1]
            solution[len_nums-i-2] *= post_product
        
        return solution




result = Solution()
nums = [-1,1,0,-3,3]
output = result.productExceptSelf(nums)
print("output", output)
expected = [0,0,9,0,0]
if output == expected:
    print("Test passed successfully!")
class Solution(object):
    def canJump(self, nums):
        len_nums = len(nums) -1
        end_point = len_nums

        for i in range(len_nums - 1, -1, -1):
            if i + nums[i] >= end_point:
                end_point = i
        
        return end_point == 0

        


result = Solution()
nums = [2, 5, 0, 0]
output = result.canJump(nums)
print(output)
expected = True
if output == expected:
    print("Test passed successfully!")

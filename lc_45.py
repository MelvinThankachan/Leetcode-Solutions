class Solution(object):
    # greedy method
    def jump(self, nums):
        len_nums = len(nums)
        jump, current, farthest = 0, 0, 0

        for i in range(len_nums - 1):
            farthest = max(farthest, nums[i] + i)
            if i == current:
                current = farthest
                jump += 1

        return jump
    
    # Dynamic programming
    def jump(self, nums):
        len_nums = len(nums)
        dp = [0] * len_nums

        for i in range(len_nums - 2, -1, -1):
            if nums[i] == 0:
                dp[i] = 1001
                continue
            
            dp[i] = 1 + min(dp[i + 1 : min(len_nums - 1, i + nums[i]) + 1])

        return dp[0]


result = Solution()
nums = [1, 2]
output = result.jump(nums)
print(f"Output: {output}")
expected = 1
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

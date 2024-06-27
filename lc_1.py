class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in num_map:
                return [num_map[need], i]
            num_map[num] = i
        return []


result = Solution()
nums = [2, 7, 11, 15]
target = 9
output = result.twoSum(nums, target)
print(output)
expected_output = [0, 1]
if output == expected_output:
    print("Jayichu mwone!")

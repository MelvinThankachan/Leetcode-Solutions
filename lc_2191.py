# 2191. Sort the Jumbled Numbers


class Solution:
    def sortJumbled(self, mapping, nums):
        map = []
        for i, num in enumerate(nums):
            num = str(num)
            new_num = 0
            for n in num:
                new_num *= 10
                new_num += mapping[int(n)]
            map.append((new_num, i))
        map.sort()
        l = len(nums)
        return [nums[map[i][1]] for i in range(l)]


result = Solution()
mapping = [5,6,8,7,4,0,3,1,9,2]
nums = [7686,97012948,84234023,2212638,99]
output = result.sortJumbled(mapping, nums)
print(output)
expected = [99,7686,2212638,97012948,84234023]
if output == expected:
    print("jayichu mone!")
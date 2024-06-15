class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        uniq = {}

        for num in nums[:]:
            if num in uniq:
                uniq[num] += 1
            else:
                uniq[num] = 1

            if uniq[num] > 2:
                nums.remove(num)
            else:
                k += 1
            
        return k

result = Solution()
nums = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5]
output = result.removeDuplicates(nums)
print(output)

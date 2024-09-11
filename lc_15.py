# 3Sum

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        output = []

        for i, first_num in range(n - 2):
            if i > 0 and first_num == nums[i-1]:
                continue

            left = i + 1
            right = n - 1
            
            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                three_sum = first_num + left_num + right_num 
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    output.append([first_num, left_num, right_num])

        
        return output


result = Solution()
nums = [-1,0,1,2,-1,-4]
output = result.threeSum(nums)
print(f"Output: {output}")
expected = [[-1,-1,2],[-1,0,1]]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


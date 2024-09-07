class Solution(object):
    def rotate(self, nums, k):
        nums_lenth = len(nums)
        print(nums_lenth, k, nums_lenth // 2)
        if k > nums_lenth:
            k = k % nums_lenth
        temp_list = nums[: nums_lenth - k]
        print(temp_list)
        nums[:k] = nums[nums_lenth - k :]
        nums[k:] = temp_list

        return nums


result = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 6
output = result.rotate(nums, k)
print(f"Output: {output}")
expected = [4, 5, 6, 7, 1, 2, 3]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


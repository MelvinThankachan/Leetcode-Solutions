# 912. Sort an Array


class Solution:
    def sortArray(self, nums):
        # Merge Sort
        n = len(nums)
        if n <= 1:
            return nums

        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merging
        l = 0
        r = 0
        i = 0
        left_n = len(left)
        right_n = len(right)
        while l < left_n and r < right_n:
            if left[l] <= right[r]:
                nums[i] = left[l]
                l += 1
            else:
                nums[i] = right[r]
                r += 1
            i += 1
        while l < left_n:
            nums[i] = left[l]
            l += 1
            i += 1
        while r < right_n:
            nums[i] = right[r]
            r += 1
            i += 1

        return nums


result = Solution()
nums = [5, 1, 1, 2, 0, 0]
output = result.sortArray(nums)
print(output)
expected = [0, 0, 1, 1, 2, 5]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


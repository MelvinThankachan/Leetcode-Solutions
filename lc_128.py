# 128. Longest Consecutive Sequence


from typing import List


class Solution:
    # My solution O(n log n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        prev = nums[0] - 1
        length = longest = 0
        for num in nums:
            length = length + 1 if num == prev + 1 else 1
            prev = num
            longest = max(longest, length)
        return longest

    # O(n) solution
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest


result = Solution()
nums = [1, 2, 0, 1]
output = result.longestConsecutive(nums)
print(output)
expected = 3
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

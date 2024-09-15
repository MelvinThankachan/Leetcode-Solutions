# 2215. Find the Difference of Two Arrays


from typing import List


class Solution:
    # def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    #     distinct1 = []
    #     distinct2 = []
    #     for num in nums1:
    #         if num not in nums2 and num not in distinct1:
    #             distinct1.append(num)
    #     for num in nums2:
    #         if num not in nums1 and num not in distinct2:
    #             distinct2.append(num)
    #     return [distinct1, distinct2]

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]


result = Solution()
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
output = result.findDifference(nums1, nums2)
print(f"Output: {output}")
expected = [[1, 3], [4, 6]]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

# 108. Convert Sorted Array to Binary Search Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        length = len(nums)
        if length == 0:
            return None
        mid = length // 2
        new_node = TreeNode(nums[mid])
        new_node.left = self.sortedArrayToBST(nums[:mid])
        new_node.right = self.sortedArrayToBST(nums[mid+1:])
        return new_node


result = Solution()
nums = [-10,-3,0,5,9]
result.sortedArrayToBST(nums)

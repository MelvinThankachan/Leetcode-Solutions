# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node):
            return node.left is None and node.right is None

        def in_order(root, sum=0):
            if root is None:
                return False
            sum += root.val
            if sum == targetSum and is_leaf(root):
                return True
            left = in_order(root.left, sum)
            right = in_order(root.right, sum)
            return left or right

        return in_order(root)

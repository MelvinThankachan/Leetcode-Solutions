# 236. Lowest Common Ancestor of a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from tree_template import TreeNode, create_tree_from_array, get_node
from collections import deque


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


result = Solution()
root = create_tree_from_array([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = get_node(root, 5)
q = get_node(root, 4)
targetSum = 8
output = result.lowestCommonAncestor(root, p, q)
print(f"Output: {output.val if output else "None"}")
expected = get_node(root, 5)
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

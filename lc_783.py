# 783. Minimum Distance Between BST Nodes


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDiffInBST(self, root):
        min_value = float("inf")
        prev_node = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nonlocal min_value, prev_node
            if prev_node is not None:
                min_value = min(min_value, abs(node.val - prev_node.val))
            prev_node = node
            inorder(node.right)

        inorder(root)
        return min_value

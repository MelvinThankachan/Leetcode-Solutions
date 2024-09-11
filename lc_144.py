# 144. Binary Tree Preorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def pre_order(root):
            if root is None:
                return
            result.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        result = []
        pre_order(root)
        return result

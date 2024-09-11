# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = 0
        node = root
        while node is not None:
            left_height += 1
            node = node.left

        right_height = 0
        node = root
        while node is not None:
            right_height += 1
            node = node.right

        if left_height == right_height:
            return pow(2, left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         left_node = root
#         right_node = root
#         left_height = 0
#         right_height = 0
#         while left_node is not None:
#             left_node = left_node.left
#             left_height += 1
#         while right_node is not None:
#             right_node = right_node.right
#             right_height += 1
#         if left_height == right_height:
#             return pow(2, left_height) - 1
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# 530. Minimum Absolute Difference in BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.min_value = float("inf")
        self.prev_value = None

    def getMinimumDifference(self, root):
        def get_minimum_diff(root):
            if root is None:
                return

            get_minimum_diff(root.left)

            if self.prev_value is not None:
                self.min_value = min(self.min_value, abs(root.val - self.prev_value))

            self.prev_value = root.val

            get_minimum_diff(root.right)

        get_minimum_diff(root)
        return self.min_value

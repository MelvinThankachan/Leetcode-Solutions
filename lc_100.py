# 100. Same Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)
        return p.val == q.val and left_check and right_check

# 101. Symmetric Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSymmetric(self, root):
        def mirror(tree1, tree2):
            if tree1 is None or tree2 is None:
                return tree1 == tree2

            if tree1.val != tree2.val:
                return False
            return mirror(tree1.left, tree2.right) and mirror(tree1.right, tree2.left)

        return mirror(root.left, root.right)

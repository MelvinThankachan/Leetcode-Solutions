# 110. Balanced Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from tree_template import TreeNode, create_tree_from_array


# My solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root):
            height = 0
            if root is not None:
                left_height = get_height(root.left)
                right_height = get_height(root.right)
                height = max(left_height, right_height) + 1
            if root not in heights:
                heights[root] = height
            return height

        def is_balanced(root):
            if root is None:
                return True
            left = root.left
            left_height = heights[left] if left in heights else get_height(left)
            right = root.right
            right_height = heights[right] if right in heights else get_height(right)
            balanced = abs(left_height - right_height) <= 1
            return is_balanced(left) and is_balanced(right) and balanced

        heights = {}
        return is_balanced(root)


# Best solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def Height(root):
            if root is None:
                return 0
            left_height = Height(root.left)
            right_height = Height(root.right)
            if (
                left_height < 0
                or right_height < 0
                or abs(left_height - right_height) > 1
            ):
                return -1
            return max(left_height, right_height) + 1

        return Height(root) >= 0


result = Solution()
array = [3, 9, 20, None, None, 15, 7]
root = create_tree_from_array(array)
output = result.isBalanced(root)
print(f"Output: {output}")
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


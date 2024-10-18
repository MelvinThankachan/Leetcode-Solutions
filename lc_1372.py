# 1372. Longest ZigZag Path in a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from tree_template import TreeNode, create_tree_from_array


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def dfs(node, dir, length=1):
            if not node:
                return

            nonlocal max_length
            max_length = max(max_length, length)

            dfs(node.left, "left", length + 1 if dir == "right" else 1)
            dfs(node.right, "right", length + 1 if dir == "left" else 1)

        if not root:
            return max_length
        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)
        return max_length


result = Solution()
root = create_tree_from_array([1, 1, 1, None, 1, None, None, 1, 1, None, 1])
targetSum = 8
output = result.longestZigZag(root)
print(f"Output: {output}")
expected = 4
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

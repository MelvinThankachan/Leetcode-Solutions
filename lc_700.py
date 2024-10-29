# 700. Search in a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from tree_template import TreeNode, create_tree_from_array, tree_to_level_order


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)


result = Solution()
root = create_tree_from_array([4, 2, 7, 1, 3])
val = 2
output = tree_to_level_order(result.searchBST(root, val))
print(f"Output: {output}")
expected = [2, 1, 3]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

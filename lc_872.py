# 872. Leaf-Similar Trees


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from tree_template import TreeNode, create_tree_from_array


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leafs(root, leafs):
            if root is None:
                return
            if root.left is None and root.right is None:
                leafs.append(root.val)
                return
            get_leafs(root.left, leafs)
            get_leafs(root.right, leafs)

        leafs1 = []
        leafs2 = []
        get_leafs(root1, leafs1)
        get_leafs(root2, leafs2)
        return leafs1 == leafs2


result = Solution()
root1 = create_tree_from_array([1, 2, 3])
root2 = create_tree_from_array([1, 3, 2])
output = result.leafSimilar(root1, root2)
print(f"Output: {output}")
expected = False
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

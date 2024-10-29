# 450. Delete Node in a BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from tree_template import (
    TreeNode,
    create_tree_from_array,
    tree_to_level_order,
    get_node,
)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            max_node = root.left
            while max_node.right is not None:
                max_node = max_node.right
            root.val = max_node.val
            root.left = self.deleteNode(root.left, max_node.val)

        return root


result = Solution()
root = create_tree_from_array([5, 3, 6, 2, 4, None, 7])
key = 3
output = result.deleteNode(root, key)
print(f"Output: {tree_to_level_order(output)}")
output = get_node(root=output, node_value=key)
if output is None:
    print("Test passed successfully!")
else:
    print("Test failed!")

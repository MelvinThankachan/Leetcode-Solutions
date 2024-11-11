# 111. Minimum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from tree_template import TreeNode, create_tree_from_array
from collections import deque


class Solution:
    # My Solution
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([root])
        depth = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                curr_node = queue.popleft()

                if curr_node.left is None and curr_node.right is None:
                    return depth
                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)

            depth += 1

        return depth

    # Better Solution
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([(root, 1)])

        while queue:
            curr_node, curr_depth = queue.popleft()

            if curr_node.left is None and curr_node.right is None:
                return curr_depth
            if curr_node.left is not None:
                queue.append((curr_node.left, curr_depth + 1))
            if curr_node.right is not None:
                queue.append((curr_node.right, curr_depth + 1))


result = Solution()
root = create_tree_from_array([1, 2, 3, 4, 5])
output = result.minDepth(root)
print(f"Output: {output}")
expected = 2
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

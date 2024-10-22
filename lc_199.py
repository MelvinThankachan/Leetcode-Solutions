# 199. Binary Tree Right Side View


# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional, List
from tree_template import TreeNode, create_tree_from_array


class Solution:
    # Iterative Solution
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        current_level = deque([root])
        next_level = deque()
        value = 0
        while len(current_level) > 0:
            root = current_level.popleft()
            if root is not None:
                value = root.val
            left = root.left
            right = root.right
            if left is not None:
                next_level.append(left)
            if right is not None:
                next_level.append(right)
            if len(current_level) == 0:
                result.append(value)
                current_level = next_level
                next_level = deque()
        return result

    # Recursive Solution
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}

        def dfs(root, level=1):
            if root is None:
                return

            if level not in levels:
                levels[level] = root.val

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root)
        return list(levels.values())


result = Solution()
root = create_tree_from_array([1, 2, 3, None, 5, None, 4])
output = result.rightSideView(root)
print(f"Output: {output}")
expected = [1, 3, 4]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

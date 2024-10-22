# 1161. Maximum Level Sum of a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from tree_template import TreeNode, create_tree_from_array
from collections import deque, defaultdict
from typing import Optional


class Solution:
    # Iterative Solution
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_sum = float("-inf")
        max_level = 1
        current_level = 1

        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1

        return max_level

    # Recursive Solution
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        level_sums = defaultdict(int)

        def dfs(node, level):
            if node is None:
                return

            level_sums[level] += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)

        max_level = max(level_sums, key=level_sums.get)

        return max_level


result = Solution()
root = create_tree_from_array([-100, -200, -300, -20, -5, -10, None])
output = result.maxLevelSum(root)
print(f"Output: {output}")
expected = 3
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from tree_template import TreeNode, create_tree_from_array
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, curr_sum=0):
            count = 0
            if root:
                curr_sum += root.val
                count = sums[curr_sum - targetSum]
                sums[curr_sum] += 1
                count += dfs(root.left, curr_sum) + dfs(root.right, curr_sum)
                sums[curr_sum] -= 1
            return count

        sums = defaultdict(int)
        sums[0] = 1
        return dfs(root)


result = Solution()
root = create_tree_from_array([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
targetSum = 8
output = result.pathSum(root, targetSum)
print(f"Output: {output}")
expected = 3
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

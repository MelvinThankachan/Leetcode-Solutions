# 1448. Count Good Nodes in Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from tree_template import TreeNode, create_tree_from_array


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_node, count=0):
            if root is None:
                return 0
            if root.val >= max_node:
                count += 1
                max_node = root.val
            count += dfs(root.left, max_node)
            count += dfs(root.right, max_node)
            return count

        return dfs(root, root.val)


result = Solution()
root = create_tree_from_array([3, 1, 4, 3, None, 1, 5])
output = result.goodNodes(root)
print(f"Output: {output}")
expected = 4
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

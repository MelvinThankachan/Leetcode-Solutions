# 199. Binary Tree Right Side View

from tree_template import Tree, deque

# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root):
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


tree = Tree()
tree.update([1, 2, 3, None, 5, 6, None, 4])


result = Solution()
output = result.rightSideView(tree.root)
print(output)
expected = [1, 3, 6, 4]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


# 637. Average of Levels in Binary Tree

from tree_template import Tree


class Solution:
    def averageOfLevels(self, root):
        result = []
        current_level = []
        current_level.append(root)
        next_level = []
        while len(current_level) != 0:
            level_sum = 0
            level_count = 0
            for node in current_level:
                level_sum += node.val
                level_count += 1
                left = node.left
                if left is not None:
                    next_level.append(left)
                right = node.right
                if right is not None:
                    next_level.append(right)
            result.append(level_sum / level_count)
            current_level = next_level
            next_level = []
        return result


tree = Tree()
root = [3, 9, 20, 15, 7]
tree.update(root)
# print(tree.count())
# tree.print_tree()

result = Solution()
output = result.averageOfLevels(tree.root)
print(f"Output: {output}")
expected = [3.00000, 14.50000, 11.00000]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")


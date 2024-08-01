from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def update(self, array):
        if not array:
            self.root = None
            return

        # Create the root of the tree
        self.root = TreeNode(array[0])
        queue = deque([self.root])

        index = 1

        while index < len(array):
            current = queue.popleft()

            # Add left child
            if index < len(array) and array[index] is not None:
                current.left = TreeNode(array[index])
                queue.append(current.left)
            index += 1

            # Add right child
            if index < len(array) and array[index] is not None:
                current.right = TreeNode(array[index])
                queue.append(current.right)
            index += 1

    def count(self):
        def counting(root):
            if root is None:
                return 0
            return 1 + counting(root.left) + counting(root.right)

        return counting(self.root)

    def print_tree(self):
        queue = deque([self.root])
        tree = []
        count = self.count()

        while count > 0:
            current = queue.popleft()
            value = None
            if current is not None:
                value = current.val
                queue.append(current.left)
                queue.append(current.right)
                count -= 1
            tree.append(value)

        print(tree)

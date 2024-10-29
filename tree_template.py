Used_in = [
    100,
    101,
    104,
    108,
    110,
    112,
    144,
    199,
    222,
    226,
    236,
    437,
    530,
    783,
    872,
    1372,
    1448,
]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_from_array(arr):
    """Create a binary tree from a given array using level-order traversal."""
    if not arr:
        return None

    # Create the root node
    root = TreeNode(arr[0])
    queue = [root]
    index = 1

    # Level-order traversal to create the tree
    while index < len(arr):
        node = queue.pop(0)

        # Assign left child
        if index < len(arr) and arr[index] is not None:
            node.left = TreeNode(arr[index])
            queue.append(node.left)
        index += 1

        # Assign right child
        if index < len(arr) and arr[index] is not None:
            node.right = TreeNode(arr[index])
            queue.append(node.right)
        index += 1

    return root


def print_tree(root):
    """Print the binary tree in level-order traversal."""
    if not root:
        print([])
        return
    result = []
    queue = [root]
    while queue:
        level = []
        level_length = len(queue)
        for _ in range(level_length):
            node = queue.pop(0)
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        # Remove trailing None values for a cleaner output
        if any(v is not None for v in level):
            result.append(level)
    print(result)


def tree_to_level_order(root):
    """Serialize the tree into a list of values in level-order traversal."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for a cleaner comparison
    while result and result[-1] is None:
        result.pop()
    return result


def is_tree_equal(root, arr):
    """Check if the binary tree matches the given list of values in level-order traversal."""
    tree_values = tree_to_level_order(root)
    return tree_values == arr


def get_node(root, node_value):
    """Find and return the node with the specified value."""
    if root is None or root.val == node_value:
        return root

    return get_node(root.left, node_value) or get_node(root.right, node_value)

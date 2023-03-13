def print_binary_tree(node, prefix='', is_left=True):
    """
    Prints a binary tree starting from the given node.
    """
    if node is not None:
        print(prefix + ('└── ' if is_left else '┌── ') + str(node.value))
        child_prefix = prefix + ('    ' if is_left else '│   ')
        print_binary_tree(node.left, child_prefix, True)
        print_binary_tree(node.right, child_prefix, False)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# create a binary tree
root = Node(1,
    Node(2,
        Node(4),
        Node(5)),
    Node(3,
        Node(6),
        Node(7)))

# print the binary tree
print_binary_tree(root)

def print_tree(node, prefix='', is_last=True):
    """
    Prints a tree starting from the given node.
    """
    if node==None: return
    
    print(prefix + ('└── ' if is_last else '├── ') + str(node))
    children = getattr(node, 'children', [])
    for i, child in enumerate(children):
        is_last_child = (i == len(children) - 1)
        child_prefix = prefix + ('    ' if is_last else '│   ')
        print_tree(child, child_prefix, is_last_child)

# ================================================================

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.children = [left, right]
    def __str__(self):
        try:
            return str(self.value)
        except:
            return ""
            

# create a binary tree
root = Node(1,
    Node(2,
        Node(4),
        Node(5)),
    Node(3,
        Node(6),
        Node(7)))

# print the tree
print_tree(root)

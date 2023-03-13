class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)


def list_to_tree(lst, arity):
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        for j in range(arity):
            if i < len(lst):
                child = TreeNode(lst[i])
                node.children.append(child)
                queue.append(child)
                i += 1
    return root

def print_tree(root, level=0, branch=""):
    if root:
        indent = " " * level * 4
        if not branch:
            print(indent + str(root))
        else:
            print(indent + branch + str(root))
        if len(root.children) > 1:
            branch = "├── "
        else:
            branch = "└── "
        for i, child in enumerate(root.children):
            if i == len(root.children) - 1:
                print_tree(child, level + 1, "    " + indent + branch)
            else:
                print_tree(child, level + 1, "│   " + indent + branch)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arity = 3
root = list_to_tree(lst, arity)

print_tree(root)

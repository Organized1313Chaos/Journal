class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nodes, index):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = buildTree(nodes, 2*index + 1)
    root.right = buildTree(nodes, 2*index + 2)
    return root

nodes = [1,2,2,None,3,None,3]
root = buildTree(nodes, 0)

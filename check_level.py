class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check(root):
    leaf_level = [-1]

    def solve(node, level):
        if node is None:
            return True

        if node.left is None and node.right is None:
            if leaf_level[0] == -1:
                leaf_level[0] = level
            return level == leaf_level[0]

        return (solve(node.left, level + 1) and
                solve(node.right, level + 1))

    return 1 if solve(root, 0) else 0
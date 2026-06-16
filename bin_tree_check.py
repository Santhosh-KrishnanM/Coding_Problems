class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(root, low=float('-inf'), high=float('inf')):
    if root is None:
        return True

    if root.data <= low or root.data >= high:
        return False

    return (isBST(root.left, low, root.data) and
            isBST(root.right, root.data, high))


root = Node(2)
root.left = Node(1)
root.right = Node(3)

print(1 if isBST(root) else 0)
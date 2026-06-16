class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None
        self.head = None

    def bToDLL(self, root):
        if root is None:
            return

        self.bToDLL(root.left)

        if self.prev is None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root

        self.prev = root

        self.bToDLL(root.right)

        return self.head
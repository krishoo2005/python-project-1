#level order transversal code 

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# Create Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal:")
level_order(root)
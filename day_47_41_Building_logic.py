class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1


# Create Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.left.left = Node(6)
root.left.right.right = Node(78)

root.left.left.left.left = Node(90)
root.left.right.right.right = Node              (78)

print("Height of Tree:", height(root))
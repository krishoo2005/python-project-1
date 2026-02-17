class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_iterative(root):
    stack = []
    current = root

    while stack or current:

        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")

        current = current.right


# Create Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal (Iterative):")
inorder_iterative(root)

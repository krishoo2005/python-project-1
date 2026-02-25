#mirror binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirror(root):
    if root is None:
        return None

    # Swap left and right
    root.left, root.right = root.right, root.left

    # Recursively mirror subtrees
    mirror(root.left)
    mirror(root.right)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Create Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Original Inorder:")
inorder(root)

mirror(root)

print("\nMirror Inorder:")
inorder(root)
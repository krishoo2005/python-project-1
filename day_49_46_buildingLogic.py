class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def diameter(root):
    if root is None:
        return 0

    # Height of left and right subtree
    left_height = height(root.left)
    right_height = height(root.right)

    # Diameter passing through root
    root_diameter = left_height + right_height + 1

    # Diameter of left and right subtree
    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    # Return maximum
    return max(root_diameter, left_diameter, right_diameter)


# Create Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Diameter of Tree:", diameter(root))
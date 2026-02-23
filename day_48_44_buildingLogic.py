class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_leaf_nodes(root):
    if root is None:
        return 0

    # If both left and right are None → leaf node
    if root.left is None and root.right is None:
        return 1

    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


# Create Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Leaf Nodes:", count_leaf_nodes(root))
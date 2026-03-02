class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter(root):
    max_diameter = 0

    def height(node):
        nonlocal max_diameter
        
        if node is None:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Update diameter
        max_diameter = max(max_diameter, left_height + right_height)
        
        return max(left_height, right_height) + 1

    height(root)
    return max_diameter


# -------- TEST --------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameter(root))
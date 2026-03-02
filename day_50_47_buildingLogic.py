#check if tree height  balanced 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_balanced(root):

    def check_height(node):
        if node is None:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_height(root) != -1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(is_balanced(root))
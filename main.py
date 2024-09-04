class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# In-order traversal
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)

# Pre-order traversal
def pre_order_traversal(root):
    if root:
        print(root.val, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

# Post-order traversal
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=" ")

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(40)
root.left.right = Node(20)
root.right.left = Node(60)
root.right.right = Node(80)

# Task 1: In-order traversal
print("In-order Traversal: ")
in_order_traversal(root)
print()

# Task 2: Pre-order traversal
print("Pre-order Traversal: ")
pre_order_traversal(root)
print()

# Task 3: Post-order traversal
print("Post-order Traversal: ")
post_order_traversal(root)
print()

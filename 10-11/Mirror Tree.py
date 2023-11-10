class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def mirror_tree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Original Inorder Traversal:")
inorder_traversal(root)
mirror_tree(root)
print("\nMirror Inorder Traversal:")
inorder_traversal(root)
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def is_valid_BST(node: TreeNode, max_val=float("inf"), min_val=float("-inf")) -> bool:
    if node is None:  # when reached the leaf node
        return True

    if node.val >= max_val or node.val <= min_val:  # when breaking the BST rule
        return False

    return is_valid_BST(node.left, node.val, min_val) and is_valid_BST(
        node.right, max_val, node.val
    )


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# root.left.right = TreeNode(0) # add invalid node

print(is_valid_BST(root))

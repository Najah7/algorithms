class Result:
    """Result class to store the balanced and height of the tree.

    Args:
        balanced (bool): True if the tree is balanced, False otherwise.
        height (int): The height of the tree.
    """

    def __init__(self, balanced, height):
        self.balanced = balanced
        self.height = height

    def __str__(self) -> str:
        return f"Balanced: {self.balanced}, Height: {self.height}"


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced_helper(root: Node) -> Result:
    if root is None:
        return Result(True, -1)

    left_result = is_balanced_helper(root.left)
    if not left_result.balanced:
        return left_result

    right_result = is_balanced_helper(root.right)
    if not right_result.balanced:
        return right_result

    if not left_result.balanced or not right_result.balanced:
        return Result(False, -1)

    height_diff = abs(left_result.height - right_result.height)
    if height_diff > 1:
        return Result(False, -1)

    return Result(True, max(left_result.height, right_result.height) + 1)


def isBalanced(root) -> bool:
    result = is_balanced_helper(root)
    return result.balanced


N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.right = N6
print(isBalanced(N1))  # True

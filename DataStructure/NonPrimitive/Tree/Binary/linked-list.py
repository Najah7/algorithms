class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


Root = TreeNode


def two_level_perfect_tree() -> TreeNode:
    BT = TreeNode("Root")
    # level 1
    left = TreeNode("Left")
    BT.left = left
    right = TreeNode("Right")
    BT.right = right
    # level 2
    left_left = TreeNode("Left/Left")
    left.left = left_left
    left_right = TreeNode("Left/Right")
    left.right = left_right
    right_left = TreeNode("Right/Left")
    right.left = right_left
    right_right = TreeNode("Right/Right")
    right.right = right_right

    return BT


def pre_order_traversal(node: TreeNode) -> None:  # O(n)
    # if node is None: return

    if node:
        print(node.data, end="->")
        pre_order_traversal(node.left)  # O(n/2)
        pre_order_traversal(node.right)  # O(n/2)


def in_order_traversal(node: TreeNode) -> None:  # O(n)
    # if node is None: return

    if node:
        in_order_traversal(node.left)  # O(n/2)
        print(node.data, end="->")
        in_order_traversal(node.right)  # O(n/2)


def post_order_traversal(node: TreeNode) -> None:  # O(n)
    # if node is None: return

    if node:
        post_order_traversal(node.left)  # O(n/2)
        post_order_traversal(node.right)  # O(n/2)
        print(node.data, end="->")


def level_order_traversal(node: TreeNode) -> None:  # O(n)
    if node is None:
        return

    queue = [node]
    while queue:  # O(n)
        node = queue.pop(0)
        print(node.data, end="->")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def width_priority_exploration(node: TreeNode, target: str) -> bool:  # O(n)
    if node is None:
        return False

    queue = [node]
    while queue:  # O(n)
        node = queue.pop(0)
        if node.target == target:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False


def insert_node(node: TreeNode, new_node: TreeNode) -> None:  # O(n)
    if node is None:
        raise ValueError("Root is None")
    if new_node is None:
        raise ValueError("New node is None")

    queue = [node]
    while queue:  # O(n)
        node = queue.pop(0)

        if node.left is None:
            node.left = new_node
            break
        else:
            queue.append(node.left)

        if node.right is None:
            node.right = new_node
            break
        else:
            queue.append(node.right)


def get_deepest_node(node: TreeNode) -> TreeNode:  # O(n)
    if node is None:
        return None

    queue = [node]
    while queue:  # O(n)
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return node


def delete_deepest_node(node: TreeNode, deepest_node: TreeNode) -> None:  # O(n)
    if node is None:
        return None

    queue = [node]
    while queue:  # O(n)
        node = queue.pop(0)
        if node.left:
            if node.left is deepest_node:
                node.left = None
                return
            else:
                queue.append(node.left)
        if node.right:
            if node.right is deepest_node:
                node.right = None
                return
            else:
                queue.append(node.right)


def delete_node(node: TreeNode, del_node) -> None:  # O(n)
    if node is None:
        raise ValueError("Root is None")

    queue = [node]
    while queue:
        node = queue.pop(0)
        if node is del_node:
            deepest_node = get_deepest_node(node)
            node.data = deepest_node.data
            delete_deepest_node(node, deepest_node)
            return
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def clear_tree(node: TreeNode) -> None:  # O(n)
    # garbage collector will take care of the rest
    node.data = None
    node.left = None
    node.right = None


BT = two_level_perfect_tree()
deepest = get_deepest_node(BT)
delete_deepest_node(BT, deepest)

import typing as t


class Node:
    def __init__(self, key: int) -> None:
        self.data = key
        self.left = None
        self.right = None


def min_node(node: t.Union[Node, None]) -> t.Union[Node, None]:
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(node: Node, data: int) -> Node:
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            tmp = insert(node.left, data)
            node.left = tmp
            tmp.parent = node
        else:
            tmp = insert(node.right, data)
            node.right = tmp
            tmp.parent = node
        return node


def in_order_successor(root: t.Union[Node, None], node: Node) -> t.Union[Node, None]:
    if node.right:
        return min_node(node.right)

    parent = node.parent
    while parent:
        if node != parent.right:
            break
        node = parent
        parent = parent.parent
    return parent


root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.left.right

successor = in_order_successor(root, temp)

if successor is not None:
    print(f"In order successor of {temp.data} is {successor.data}")
else:
    print(f"In order successor does not exist for {temp.data}")

import typing as t


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def does_node_exist(node: Node, value: t.Any) -> bool:
    if node is None:
        return False
    if node.value == value:
        return True
    return does_node_exist(node.left, value) or does_node_exist(node.right, value)


def find_first_common_ancestor(n1: Node, n2: Node, root: Node) -> t.Union[Node, None]:
    n1_on_left = does_node_exist(root.left, n1.value)
    n2_on_left = does_node_exist(root.left, n2.value)
    if n1_on_left ^ n2_on_left:
        return root
    elif n1_on_left:
        return find_first_common_ancestor(n1, n2, root.left)
    elif n2_on_left:
        return find_first_common_ancestor(n1, n2, root.right)


node54 = Node(54)
node88 = Node(88, node54)
node35 = Node(35)
node22 = Node(22, node35, node88)
node33 = Node(33)
node90 = Node(90, None, node33)
node95 = Node(95)
node99 = Node(99, node90, node95)
node44 = Node(44, node22, node99)
node77 = Node(77)
root = Node(55, node44, node77)

common_ancestor = find_first_common_ancestor(node88, node33, root)
print(common_ancestor.value)

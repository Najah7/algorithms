import typing as t


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class BinaryTreeNode:
    """Binary Tree

    Arg:
        val(int): The value of the node.
        left(BinaryTreeNode): The left child of the node.
        right(BinaryTreeNode): The right child of the node.
    """

    def __init__(self, val):
        self.val = val
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None


def depth(tree: BinaryTreeNode) -> int:
    if tree is None:
        return 0
    if tree.right is None and tree.left is None:
        return 1
    else:
        left_height = 1 + depth(tree.left)
        right_height = 1 + depth(tree.right)
        return max(left_height, right_height)


def tree_to_linkedlist(
    root: BinaryTreeNode, custDict: t.Dict[int, LinkedList] = {}, d: int = None
) -> t.Dict[int, LinkedList]:
    if d is None:
        d = depth(root)
    if custDict.get(d) is None:
        custDict[d] = LinkedList(root.val)
    else:
        custDict[d].add(root.val)
        if d == 1:
            return custDict
    if root.left:
        tree_to_linkedlist(root.left, custDict, d - 1)
    if root.right:
        tree_to_linkedlist(root.right, custDict, d - 1)
    return custDict


root = BinaryTreeNode(1)
two = BinaryTreeNode(2)
three = BinaryTreeNode(3)
four = BinaryTreeNode(4)
five = BinaryTreeNode(5)
six = BinaryTreeNode(6)
seven = BinaryTreeNode(7)
root.left = two
root.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custom_dict = tree_to_linkedlist(root)
for level, list in custom_dict.items():
    print(f"Level {level}: {list}")

class BSTNode:
    def __init__(self, value) -> None:
        if value is None:
            raise ValueError("Value can't be None")
        self.value = value
        self.left = None
        self.right = None

    def insert_node(self, value) -> None:  # O(log n)
        if value == self.value:
            return

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert_node(
                    value
                )  # O(log n) <- (log2 n) is the height of the tree
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert_node(value)  # O(log n)

    def pre_order_traversal(self, node) -> None:  # O(n)
        if node is None:
            return

        print(node.value, end="->")
        self.pre_order_traversal(node.left)  # O(n/2)
        self.pre_order_traversal(node.right)  # O(n/2)

    def in_order_traversal(self, node) -> None:  # O(n)
        if node is None:
            return

        self.in_order_traversal(node.left)  # O(n/2)
        print(node.value, end="->")
        self.in_order_traversal(node.right)  # O(n/2)

    def post_order_traversal(self, node) -> None:  # O(n)
        if node is None:
            return

        self.post_order_traversal(node.left)  # O(n/2)
        self.post_order_traversal(node.right)  # O(n/2)
        print(node.value, end="->")

    def level_order_traversal(self, node) -> None:  # O(n)
        if node is None:
            return

        queue = []
        queue.append(node)

        while len(queue) > 0:  # O(n)
            print(queue[0].value, end="->")
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def search(self, node, value) -> bool:  # O(log n)
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self.search(node.left, value)  # O(log n)
        else:
            return self.search(node.right, value)  # O(log n)

    def min_value_node(self, node) -> int:  # O(log n)
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, node, del_node) -> None:  # O(n) θ(log n)
        if node is None:
            return node

        if del_node < node.value:
            node.left = self.delete_node(node.left, del_node)  # O(n/2)
        elif del_node > node.value:
            node.right = self.delete_node(node.right, del_node)  # O(n/2)
        else:  # when node.value == del_node.value
            if node.left is None:  # node has only right child and no children
                tmp = node.right
                node = None
                return tmp
            elif node.right is None:  # node has only left child
                tmp = node.left
                node = None
                return tmp

            # node has both left and right children
            node.value = self.min_value_node(node.right).value  # O(log n)
            node.right = self.delete_node(
                node.right, node.value
            )  # O(n/2) <- This n is not the same as the previous n
        return node

    def clear(self, root) -> None:  # O(1)
        root = None
        root.left = None
        root.right = None


def sample_BST():
    BST = BSTNode(10)
    BST.insert_node(5)
    BST.insert_node(15)
    BST.insert_node(7)
    BST.insert_node(12)
    BST.insert_node(20)
    BST.insert_node(3)
    return BST


BST = sample_BST()
print(BST.pre_order_traversal(BST))
print(BST.in_order_traversal(BST))
print(BST.post_order_traversal(BST))
print(BST.level_order_traversal(BST))

print(BST.search(BST, 100))
print(BST.delete_node(BST, 15))
print(BST.in_order_traversal(BST))

import logging
import typing as t

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AVL:
    class Node:
        def __init__(self, data) -> None:
            self.value: int = data
            self.left: t.Optional["AVL.Node"] = None
            self.right: t.Optional["AVL.Node"] = None
            self.height: int = 1

        def __str__(self) -> str:
            AVL.Traverse.level_order(self)
            return ""

    @staticmethod
    def get_height(node: "AVL.Node") -> int:
        if node is None:
            return 0
        return node.height

    @staticmethod
    def get_balance(node: "AVL.Node") -> int:
        """Get the balance factor of a node
        return:
            1 < retval => Left heavy

            -1 < retval < 1 => Balanced

            retval < -1 => Right heavy
        """
        if node is None:
            return 0
        return AVL.get_height(node.left) - AVL.get_height(node.right)

    @staticmethod
    def get_min_value_node(node: "AVL.Node") -> "AVL.Node":
        current = node
        while current.left is not None:
            current = current.left
        return current

    class Traverse:
        @staticmethod
        def pre_order(
            node: "AVL.Node",
        ) -> None:  # O(n) <- visit each node once, so O(n)
            if node is None:
                return

            print(node.value, end=" ")
            AVL.Traverse.pre_order(node.left)
            AVL.Traverse.pre_order(node.right)

        @staticmethod
        def in_order(node: "AVL.Node") -> None:  # O(n)
            if node is None:
                return

            AVL.Traverse.in_order(node.left)
            print(node.value, end=" ")
            AVL.Traverse.in_order(node.right)

        @staticmethod
        def post_order(node: "AVL.Node") -> None:  # O(n)
            if node is None:
                return

            AVL.Traverse.post_order(node.left)
            AVL.Traverse.post_order(node.right)
            print(node.value, end=" ")

        @staticmethod
        def level_order(AVL_node: "AVL.Node") -> None:  # O(n)
            if AVL_node is None:
                return
            queue = [AVL_node]
            while queue:
                node = queue.pop(0)
                print(node.value, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    class Operations:
        @staticmethod
        def search(node: "AVL.Node", data: int) -> bool:
            if node is None:
                return False
            if node.value == data:
                return True
            if data < node.value:
                return AVL.Operations.search(node.left, data)
            else:
                return AVL.Operations.search(node.right, data)

        @staticmethod
        def insert(tree: "AVL.Node", data: t.Union[list, int]):  # O(n log n)
            if isinstance(data, int):
                return AVL.Operations._insert_value(tree, data)
            elif isinstance(data, list):
                for datum in data:  # O(n)
                    logger.info(f"Inserting {datum}")
                    AVL.Traverse.level_order(tree)
                    print()
                    tree = AVL.Operations._insert_value(tree, datum)  # O(log n)
                return tree

        @staticmethod
        def delete(node: "AVL.Node", value: int):  # O(log n)
            if node is None:
                return node

            if value < node.value:
                node.left = AVL.Operations.delete(node.left, value)  # O(log n)
            elif value > node.value:
                node.right = AVL.Operations.delete(node.right, value)  # O(log n)
            else:  # when found the node to delete
                if node.left is None:  # node has only right child or no child
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:  # node has only left child
                    temp = node.left
                    node = None
                    return temp
                temp = AVL.get_min_value_node(node.right)  # O(log n)
                node.value = temp.value
                node.right = AVL.Operations.delete(node.right, temp.value)  # O(log n)

            node.height = 1 + max(AVL.get_height(node.left), AVL.get_height(node.right))
            return AVL.Operations.balance(node, value)

        @staticmethod
        def clear(node: "AVL.Node") -> None:  # O(1)
            if node is None:
                return

            AVL.Operations.clear(node.left)
            AVL.Operations.clear(node.right)
            node = None

        @staticmethod
        def balance(node: "AVL.Node", value: int):  # O(1)
            if AVL.Conditions.is_LL(node, value):
                return AVL.Rotations.right(node)
            elif AVL.Conditions.is_RR(node, value):
                return AVL.Rotations.left(node)
            elif AVL.Conditions.is_LR(node, value):
                return AVL.Rotations.left_right(node)
            elif AVL.Conditions.is_RL(node, value):
                return AVL.Rotations.right_left(node)
            return node

        @staticmethod
        def _insert_value(node: "AVL.Node", value: int):  # O(log n)
            if node is None:
                return AVL.Node(value)

            if value < node.value:
                node.left = AVL.Operations._insert_value(node.left, value)  # O(log n)
            else:
                node.right = AVL.Operations._insert_value(node.right, value)  # O(log n)

            node.height = 1 + max(AVL.get_height(node.left), AVL.get_height(node.right))

            return AVL.Operations.balance(node, value)

    class Conditions:
        @staticmethod
        def is_RR(disbalanced_node: "AVL.Node", value: int):  # O(1)
            balance = AVL.get_balance(disbalanced_node)
            return balance < -1 and disbalanced_node.right.value < value

        @staticmethod
        def is_LL(disbalanced_node: "AVL.Node", value: int):  # O(1)
            balance = AVL.get_balance(disbalanced_node)
            return 1 < balance and value < disbalanced_node.left.value

        @staticmethod
        def is_LR(disbalanced_node: "AVL.Node", value: int):  # O(1)
            balance = AVL.get_balance(disbalanced_node)
            return 1 < balance and disbalanced_node.left.value < value

        @staticmethod
        def is_RL(disbalanced_node: "AVL.Node", value: int):  # O(1)
            balance = AVL.get_balance(disbalanced_node)
            return balance < -1 and value < disbalanced_node.right.value

    class Rotations:
        # when Left-Left condition
        @staticmethod
        def right(disbalanced_node: "AVL.Node"):  # O(1)
            new_node = disbalanced_node.left
            disbalanced_node.left = disbalanced_node.left.right
            new_node.right = disbalanced_node
            disbalanced_node.height = 1 + max(
                AVL.get_height(disbalanced_node.left),
                AVL.get_height(disbalanced_node.right),
            )
            new_node.height = 1 + max(
                AVL.get_height(new_node.left), AVL.get_height(new_node.right)
            )
            return new_node

        # when Right-Right condition
        @staticmethod
        def left(disbalanced_node: "AVL.Node"):  # O(1)
            new_node = disbalanced_node.right
            disbalanced_node.right = disbalanced_node.right.left
            new_node.left = disbalanced_node
            disbalanced_node.height = 1 + max(
                AVL.get_height(disbalanced_node.left),
                AVL.get_height(disbalanced_node.right),
            )
            new_node.height = 1 + max(
                AVL.get_height(new_node.left), AVL.get_height(new_node.right)
            )
            return new_node

        # when Left-Right condition
        @staticmethod
        def left_right(disbalanced_node: "AVL.Node"):  # O(1)
            disbalanced_node.left = AVL.Rotations.left(disbalanced_node.left)
            return AVL.Rotations.right(disbalanced_node)

        # when Right-Left condition
        @staticmethod
        def right_left(disbalanced_node: "AVL.Node"):  # O(1)
            disbalanced_node.right = AVL.Rotations.right(disbalanced_node.right)
            return AVL.Rotations.left(disbalanced_node)


root = AVL.Node(10)
disbalanced_data = [20, 30, 40, 50, 25]
tree = AVL.Operations.insert(root, disbalanced_data)
print(tree)

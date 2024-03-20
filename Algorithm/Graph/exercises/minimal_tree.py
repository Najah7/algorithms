import typing as t


class BSTNode:
    def __init__(
        self,
        data: t.Any,
        left: t.Union["BSTNode", None] = None,
        right: t.Union["BSTNode", None] = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right

    def display(self) -> None:
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self) -> t.List[str]:
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.data
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.data
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "%s" % self.data
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def minimal_tree(sorted_arr: t.List) -> t.Union[BSTNode, None]:
    if not sorted_arr:
        return None
    if len(sorted_arr) == 1:
        return BSTNode(sorted_arr[0])

    mid = len(sorted_arr) // 2
    left = minimal_tree(sorted_arr[:mid])
    right = minimal_tree(sorted_arr[mid + 1 :])
    return BSTNode(sorted_arr[mid], left, right)


sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree = minimal_tree(sortedArray)
tree.display()

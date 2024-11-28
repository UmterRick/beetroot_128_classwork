class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_node is None and self.left_node is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_node is None:
            lines, n, p, x = self.left_node.display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_node is None:
            lines, n, p, x = self.right_node.display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_node.display_aux()
        right, m, q, y = self.right_node.display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)

        else:
            self._insert(self.root, value)

    def _insert(self, current_root: Node, value: int):
        if value <= current_root.value:
            if current_root.left_node is None:
                current_root.left_node = Node(value)
            else:
                self._insert(current_root.left_node, value)

        elif value > current_root.value:
            if current_root.right_node is None:
                current_root.right_node = Node(value)
            else:
                self._insert(current_root.right_node, value)

    def display(self):
        lines, *_ = self.root.display_aux()
        for line in lines:
            print(line)



if __name__ == "__main__":

    tree = BinarySearchTree()

    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(7)
    tree.insert(3)
    tree.insert(12)
    tree.insert(18)
    tree.insert(20)

    tree.display()
    tree.insert(21)
    tree.insert(1)
    tree.insert(0)
    tree.insert(-1)
    tree.insert(-21)
    print("\n\n\n\n")
    tree.display()

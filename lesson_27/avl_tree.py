from bst import Node


class AVLNode(Node):
    def __init__(self, value: int):
        super().__init__(value)
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root: AVLNode, value):
        if not root:
            return AVLNode(value)

        elif value < root.value:
            if root.left_node is None:
                print(f"Add '{value}' left to {root}")
                root.left_node = AVLNode(value)
            else:
                root.left_node = self._insert(root.left_node, value)
        elif value > root.value:
            if root.right_node is None:
                print(f"Add '{value}' right to {root}")

                root.right_node = AVLNode(value)
            else:
                root.right_node = self._insert(root.right_node, value)

        root.height = 1 + max(self.get_height(root.left_node), self.get_height(root.right_node))
        balance = self.get_balance(root)

        # Right case
        if balance < -1 and value > root.right_node.value:
            print("Right side is bigger")
            print(f"Rotate left with Root -> {root}")
            return self.rotate_left(root)

        # Left case
        if balance > 1 and value < root.left_node.value:
            return self.rotate_right(root)


        # left-right case
        if balance > 1 and value > root.left_node.value:
            root.left_node = self.rotate_left(root.left_node)
            return self.rotate_right(root)



        # right-left case
        if balance < -1 and value < root.right_node.value:
            root.right_node = self.rotate_right(root.right_node)
            return self.rotate_left(root)



        return root

    def rotate_left(self, root):
        print(f"Root is {root}")

        root_right = root.right_node
        print(f"Right node: {root_right}")

        root_left = root.left_node
        print(f"Left node: {root_left}")

        root_right.left_node = root
        print(f"From now {root} is left to {root_left}")
        root.right_node = root_left
        print(f"From now {root_left} is right to {root.right_node}")

        root.height = 1 + max(self.get_height(root.left_node), self.get_height(root.right_node))
        root_right.height = 1 + max(self.get_height(root_right.left_node), self.get_height(root_right.right_node))

        return root_right

    def rotate_right(self, root):
        root_left = root.left_node
        root_right = root.right_node

        root_left.right_node = root
        root.left_node = root_right

        root.height = 1 + max(self.get_height(root.left_node), self.get_height(root.right_node))
        root_left.height = 1 + max(self.get_height(root_left.left_node), self.get_height(root_left.right_node))

        return root_left

    def get_height(self, root: AVLNode):
        return root.height if root else 0

    def get_balance(self, root: AVLNode):
        if root:
            left_height = self.get_height(root.left_node)
            right_height = self.get_height(root.right_node)
            return left_height - right_height

        else:
            return 0

    def display(self):
        lines, *_ = self.root.display_aux()
        for line in lines:
            print(line)


if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(7)
    tree.insert(2)
    tree.insert(12)
    tree.insert(18)
    tree.insert(20)

    tree.display()
    tree.insert(21)
    print("\n\n")
    tree.display()

    tree.insert(2)
    print("\n\n")
    tree.display()

    tree.insert(1)
    print("\n\n")
    tree.display()

    tree.insert(0)
    print("\n\n")
    tree.display()

    tree.insert(-1)
    print("\n\n")
    tree.display()

    tree.insert(-2)
    print("\n\n")
    tree.display()

    tree.insert(-3)
    print("\n\n")
    tree.display()

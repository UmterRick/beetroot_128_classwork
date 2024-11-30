# DFS - depth search
# BFS - Width search
from collections import deque

from bst import BinarySearchTree


def dfs(root):
    if root:
        print(root, end=" -> ")
        dfs(root.left_node)
        dfs(root.right_node)


def bfs_with_queue(root):
    if not root:
        return

    queue  = deque([root])
    while queue:
        print(queue)
        node = queue.popleft()

        print(f"Get {node} from stack -> {queue}")

        # print(node, end=" -> ")
        if node.right_node:
            queue.append(node.right_node)
            print(f"Add {node.right_node} right node")
        if node.left_node:
            queue.append(node.left_node)
            print(f"Add {node.left_node} left node")

        print(queue)
        print("\n", "----" * 10, "\n")



def dfs_stack(root, search_value):
    if not root:
        return

    stack = [root]
    while stack:
        # print(stack)
        node = stack.pop()
        if node.value == search_value:
            return node
        # print(f"Get {node} from stack -> {stack}")

        print(node, end=" -> ")
        if node.right_node:
            stack.append(node.right_node)
            # print(f"Add {node.right_node} right node")
        if node.left_node:
            stack.append(node.left_node)
            # print(f"Add {node.left_node} left node")

        # print(stack)
        # print("\n", "----" * 10, "\n")



tree = BinarySearchTree()

tree.insert("D")
tree.insert("F")
tree.insert("E")
tree.insert("B")
tree.insert("A")
tree.insert("C")
tree.insert("G")

tree.display()

print()
print(tree.root)
print()
print("DFS Stack")
dfs_stack(tree.root, "R")
print()
print("DFS Recursion")
dfs(tree.root)
print()
print()
tree.display()
print("BFS Queue")
bfs_with_queue(tree.root)
print()

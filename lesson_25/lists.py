"""
LinkedList


"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node



class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0


    def append(self, data):
        new_node = Node(data) # (1, None); (2, Node(1)); (3, Node(2))
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
        self.size +=1
        return


    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next_node = self.root
            self.root = new_node
            return

        current = self.root
        current_index = 0

        while current and current_index < index - 1:
            current = current.next_node
            current_index += 1

        if not current:
            raise IndexError

        new_node.next_node = current.next_node
        current.next_node = new_node


    def __str__(self):
        n = self.root
        s = "["
        while n.next_node:
            s += str(n.data) + ", "
            n = n.next_node

        s += str(n.data) + "]"
        return s





l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
# print(l)


class DoubleNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node



class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
        new_node = DoubleNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def appendleft(self, data):
        new_node = DoubleNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def remove(self, data):
            current = self.head
            while current:
                if current.data == data:
                    if current == self.head and current == self.tail:
                        self.head = self.tail = None

                    elif current == self.head:
                        self.head = current.next_node
                        self.head.prev = None

                    elif current == self.tail:
                        self.tail = current.prev_node
                        self.tail.next = None

                    else:
                        current.prev_node.next_node = current.next_node
                        current.next_node.prev_node = current.prev_node

                    return
                current = current.next_node

    def __str__(self):
        n = self.head
        s = "["
        if n:
            while n.next_node:
                s += str(n.data) + ", "
                n = n.next_node

            s += str(n.data)
        s += "]"
        return s



double_linked_list = DoublyLinkedList()
print(double_linked_list)
double_linked_list.append(1)
print(double_linked_list)
double_linked_list.append(2)
print(double_linked_list)
double_linked_list.appendleft(0)
print(double_linked_list)
double_linked_list.appendleft(-1)
print(double_linked_list)
double_linked_list.remove(0)
print(double_linked_list)



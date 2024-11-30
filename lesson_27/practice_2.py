# Trie - prefix tree

class Node:
    def __init__(self, text = ""):
        self.text = text
        self.children = dict()
        self.is_word = False

    def __repr__(self):
        return f"Node('{self.text}')"



class Trie:
    def __init__(self):
        self.root = Node()


    def insert(self, word): # app, apple
        # app : a -> p -> p
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] =  Node(prefix)
            current = current.children[char]
        current.is_word = True

    def find(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]

        if current.is_word:
            return current
        else:
            return None


    def starts_with(self, prefix):
        words = []
        current = self.root

        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        self.__child_words_for(current, words)
        return words

    def __child_words_for(self, node, words):
        if node.is_word:
            words.append(node.text)
        for char in node.children:
            self.__child_words_for(node.children[char], words)


    def visualize(self):
        def dfs(node, depth=0):
            lines = []
            for char, child_node in node.children.items():
                lines.append(" " * (depth * 2) + f"{char}" + f"{'* ' if child_node.is_word else ''}")
                lines.extend(dfs(child_node, depth + 1))  # Recursive call for children
            return lines

        # Start DFS from root and build the representation
        result = "\n".join(dfs(self.root))
        return result if result else "Trie is empty."



tree = Trie()
tree.insert("app")
tree.insert("apple")
tree.insert("abs")
tree.insert("absorb")
tree.insert("apricot")
tree.insert("bill")
tree.insert("bills")
tree.insert("bow")
tree.insert("bowling")
tree.insert("cat")
tree.insert("caterpillar")


# print(tree.visualize())
user_input = ""
while user_input != "exit":
    user_input = input(">>> ")
    words = tree.starts_with(user_input)
    print(*words, sep=", ")



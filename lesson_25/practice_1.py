from collections import deque



class Commit:
    def __init__(self,content, message):
        self.msg = message
        self.content = content

class Editor:
    def __init__(self):
        self.text = ""
        self.history = []
        self.current_commit = -1


    def commit(self, message):
        self.history.append(Commit(self.text, message))
        self.current_commit += 1

    def add_text(self, new_chars):
        self.text += new_chars
        self.commit("ADD")

    def revert_to(self, commit_index):
        if 0 <= commit_index <= self.current_commit:
            self.text = self.history[commit_index].content
            self.current_commit = commit_index
            print(f"Reverted to {commit_index}: {self.text}")

    def undo(self):
        if self.current_commit > 0:
            self.current_commit -= 1
            self.text = self.history[self.current_commit].content
            print(f"Reverted to: {self.text}")

        else:
            print("No prev commits")

    def redo(self):
        if self.current_commit < len(self.history) - 1:
            self.current_commit += 1
            self.text = self.history[self.current_commit].content
            print(f"Redo to: {self.text}")
        else:
            print("No commits")

    def get_history(self):
        for index, commit in enumerate(self.history, 1):
            print(f"Commit {index}: {commit.content}")

editor = Editor()

editor.add_text("Hello")
editor.add_text(" ")
editor.add_text("World")
editor.get_history()
editor.undo()
editor.undo()
editor.redo()
editor.redo()
print(editor.text)
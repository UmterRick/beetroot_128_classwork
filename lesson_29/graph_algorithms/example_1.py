from collections import deque


class Graph:
    def __init__(self):
        self.vertex_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertex_dict:

            self.vertex_dict[vertex] = []



    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertex_dict and vertex_2 in self.vertex_dict:
            self.vertex_dict[vertex_1].append(vertex_2)
            if vertex_1 != vertex_2:
                self.vertex_dict[vertex_2].append(vertex_1)


    def display(self):
        for vertex, linked_vertexes in self.vertex_dict.items():
            print(f"{vertex}: {linked_vertexes}")



def depth_first_search(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, " -> ", end=" ")
            stack.extend(reversed(graph.vertex_dict[vertex]))


def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, " -> ", end=" ")
            queue.extend(graph.vertex_dict[vertex])

graph = Graph()


graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")



graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "E")
graph.add_edge("B", "D")
graph.add_edge("B", "A")
graph.add_edge("C", "D")
graph.add_edge("F", "F")


graph.display()

depth_first_search(graph, start="A")
print()
breadth_first_search(graph, start="A")

class WeightedGraph:
    def __init__(self):
        self.vertex_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertex_dict:
            self.vertex_dict[vertex] = []

    def add_edge(self, vertex_1, vertex_2, weight):
        if vertex_1 in self.vertex_dict and vertex_2 in self.vertex_dict:
            self.vertex_dict[vertex_1].append((vertex_2, weight))
            if vertex_1 != vertex_2:
                self.vertex_dict[vertex_2].append((vertex_1, weight))

    def display(self):
        for vertex, linked_vertexes in self.vertex_dict.items():
            print(f"{vertex}: {linked_vertexes}")



graph = WeightedGraph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")



graph.add_edge("A", "B", 3)
graph.add_edge("A", "C", 6, )
graph.add_edge("A", "D", 10)
graph.add_edge("B", "E", 3)
graph.add_edge("B", "D", 2)
graph.add_edge("B", "A", 13)
graph.add_edge("C", "D", 10)
graph.add_edge("F", "F", 1)


graph.display()

class CompleteGraph:
    def __init__(self, vertexes):
        self.vertex_dict = {}

        for vertex in vertexes:
            self.vertex_dict[vertex] = []

        for i in range(len(vertexes)):
            for j in range(i+1, len(vertexes)):
                self.add_edge(vertexes[i], vertexes[j])

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertex_dict and vertex_2 in self.vertex_dict:
            self.vertex_dict[vertex_1].append(vertex_2)
            if vertex_1 != vertex_2:
                self.vertex_dict[vertex_2].append(vertex_1)



    def display(self):
        for vertex, linked_vertexes in self.vertex_dict.items():
            print(f"{vertex}: {linked_vertexes}")



graph = CompleteGraph(("A", "B", "C", "D", "E"))
graph.display()
# Алгоритм Дейкстра
import heapq


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

def dijkstra_algorithm_from_to(graph: WeightedGraph, start, end):
    distances = {vertex: float('inf') for vertex in graph.vertex_dict}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    previous = {vertex: None for vertex in graph.vertex_dict}


    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex == end:
            break

        if current_vertex in visited:
            continue
        visited.add(current_vertex)


        for neighbor, weight in graph.vertex_dict[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    curr = end
    while curr is not None:
        path.insert(0, curr)
        curr = previous[curr]


    return distances[end], path


w_graph = WeightedGraph()
vertexes = ["A", "B", "C", "D", "E"]
for vertex in vertexes:
    w_graph.add_vertex(vertex)


w_graph.add_edge("A", "B", 3)
w_graph.add_edge("A", "C", 10)
w_graph.add_edge("C", "B", 2)
w_graph.add_edge("B", "E", 4)
w_graph.add_edge("C", "D", 2)
w_graph.add_edge("D", "E", 1)

w_graph.display()

for vertex in vertexes:
    shortest_distance, path = dijkstra_algorithm_from_to(w_graph, "A", vertex)
    print(f"Shortest path from A to {vertex}")
    print(f"Length: {shortest_distance}")
    print(f"Path:", " -> ".join(path))
    print("-------------" * 20)
    print()

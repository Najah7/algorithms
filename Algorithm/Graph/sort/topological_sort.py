import typing as t
from collections import defaultdict


class Graph:
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def add_edge(self, from_vertex: str, to_vertex: str):
        self.graph[from_vertex].append(to_vertex)

    def topological_sort(self):  # O(vertex + edge)
        visited = set()
        stack = []
        for vertex in list(self.graph):  # O(vertex)
            if vertex not in visited:
                self._topological_sort_explore(vertex, visited, stack)  # O(edge)
        return stack

    def _topological_sort_explore(
        self, vertex: str, visited: t.Set[str], stack: t.List[str]
    ):  # O(edge)
        visited.add(vertex)
        for neighbor in self.graph[vertex]:  # O(edge)
            if neighbor not in visited:
                self._topological_sort_explore(neighbor, visited, stack)
        stack.insert(0, vertex)


graph = Graph(8)
graph.add_edge("A", "C")
graph.add_edge("C", "E")
graph.add_edge("E", "H")
graph.add_edge("E", "F")
graph.add_edge("F", "G")
graph.add_edge("B", "D")
graph.add_edge("B", "C")
graph.add_edge("D", "F")
print(graph.topological_sort())

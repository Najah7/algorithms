from Algorithm.Graph.MinimumSpanningTree.disjointset import DisjointSet


class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        self.MST = []  # Minimum Spanning Tree

    def add_edge(self, start, dest, weight):
        self.graph.append([start, dest, weight])

    def add_node(self, node):
        self.nodes.append(node)

    def display_solution(self):
        for start, dest, weight in self.MST:
            print(f"{start} -> {dest}: {weight}")

    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])
        disjoint_set = DisjointSet(self.nodes)
        for edge in self.graph:
            start, dest, _ = edge
            if disjoint_set.find(start) != disjoint_set.find(dest):
                disjoint_set.union(start, dest)
                self.MST.append(edge)
        self.display_solution()


graph = Graph(5)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_edge("A", "B", 5)
graph.add_edge("A", "C", 13)
graph.add_edge("A", "E", 15)
graph.add_edge("B", "A", 5)
graph.add_edge("B", "C", 10)
graph.add_edge("B", "D", 8)
graph.add_edge("C", "A", 13)
graph.add_edge("C", "B", 10)
graph.add_edge("C", "E", 20)
graph.add_edge("C", "D", 6)
graph.add_edge("D", "B", 8)
graph.add_edge("D", "C", 6)
graph.add_edge("A", "B", 5)
graph.add_edge("E", "A", 15)
graph.add_edge("E", "C", 20)

graph.kruskal()

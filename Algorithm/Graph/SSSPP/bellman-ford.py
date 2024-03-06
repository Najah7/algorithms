class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, start, dest, weight):
        self.graph.append([start, dest, weight])

    def add_node(self, node):
        self.nodes.append(node)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for node in self.nodes:
            print(f"{node} \t\t {dist[node]}")

    def bellman_ford(self, start):  # O(vertex * edge)
        dist = {i: float("inf") for i in self.nodes}  # O(vertex)
        dist[start] = 0

        for _ in range(self.vertices - 1):  # O(vertex-1) -> O(vertex)
            for start, dest, weight in self.graph:  # O(edge)
                dist_to_dest = dist[start] + weight
                min_dist = min(dist[dest], dist_to_dest)
                if dist[start] != float("inf") and dist_to_dest == min_dist:
                    dist[dest] = dist_to_dest

        for start, dest, weight in self.graph:  # O(edge)
            dist_to_dest = dist[start] + weight
            min_dist = min(dist[dest], dist_to_dest)
            if dist[start] != float("inf") and dist_to_dest == min_dist:
                print("Graph contains negative cycle")
                break

        self.print_solution(dist)


graph = Graph(5)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_edge("A", "C", 6)
graph.add_edge("A", "D", 6)
graph.add_edge("B", "A", 3)
graph.add_edge("C", "D", 1)
graph.add_edge("D", "C", 2)
graph.add_edge("D", "B", 1)
graph.add_edge("E", "B", 4)
graph.add_edge("E", "D", 2)
graph.bellman_ford("E")

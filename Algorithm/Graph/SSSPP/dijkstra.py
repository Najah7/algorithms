"""Dijkstra's Algorithm"""
import heapq
import typing as t


class Edge:
    def __init__(self, weight, start: "Vertex", destination: "Vertex"):
        self.weight = weight
        self.start = start
        self.target_vertex = destination


class Vertex:
    def __init__(self, name):
        self.name: str = name
        self.visited: bool = False
        self.predecessor: t.Union[None, "Vertex"] = None
        self.neighbors: t.List[Edge] = []
        self.min_distance: float = float("inf")

    def __lt__(self, other: "Vertex"):
        return self.min_distance < other.min_distance

    def add_edge(self, weight, destination: "Vertex"):
        edge = Edge(weight, self, destination)
        self.neighbors.append(edge)


class Dijkstra:
    def __init__(self):
        self.heap: t.List[Vertex] = []

    def calculate(self, start: "Vertex"):  # O((vertex + edge) * log(vertex))
        start.min_distance = 0
        # NOTE: self.heap is empty, so we can't use heapq.heapify
        heapq.heappush(self.heap, start)  # O(1) <- first element
        while self.heap:  # O(vertex)
            current_vertex = heapq.heappop(self.heap)  # O(log(vertex))
            if current_vertex.visited:  # for avoiding cycles
                continue
            for edge in current_vertex.neighbors:  # O(edge)
                # u: current_vertex, v: target_vertex in the terminology of Dijkstra's algorithm
                u = edge.start
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(self.heap, v)  # O(log(vertex))
            current_vertex.visited = True

    def get_shortest_path(self, target: "Vertex"):  # O(vertex)
        string = ""
        string += f"Shortest path to {target.name} costs {target.min_distance}\n"
        stack = ["Done"]
        node = target
        # from the target to the start
        while node:  # O(vertex)
            stack.append(f"{node.name}->")
            node = node.predecessor
        # from the start to the target
        while stack:  # O(vertex)
            string += stack.pop()
        return string


# vertices
A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
E = Vertex("E")
F = Vertex("F")
G = Vertex("G")
H = Vertex("H")

# edges
A.add_edge(6, B)
A.add_edge(10, C)
A.add_edge(9, D)
B.add_edge(16, E)
B.add_edge(13, F)
B.add_edge(5, D)
C.add_edge(6, D)
C.add_edge(5, H)
C.add_edge(21, G)
D.add_edge(8, F)
D.add_edge(7, H)
E.add_edge(10, G)
F.add_edge(4, E)
F.add_edge(12, G)
H.add_edge(2, F)
H.add_edge(14, G)

dijkstra = Dijkstra()
dijkstra.calculate(A)
print(dijkstra.get_shortest_path(G))

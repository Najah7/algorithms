class Graph:
    def __init__(self, vertices, edges, nodes):
        self.vertices = vertices
        self.num_vertices = len(vertices)
        self.edges = edges
        self.nodes = nodes
        self.MST = []

    def display_solution(self):
        for src, dest, weight in self.MST:
            print(f"{src} -> {dest}: {weight}")

    def prims(self):  # O(vertex * edge) <- my first implementation
        visited = dict.fromkeys(self.vertices, False)
        start_vertex = self.vertices[0]
        visited[start_vertex] = True
        for _ in range(self.num_vertices - 1):  # O(vertex)
            min_edge = [None, None, float("inf")]
            for src, dest, weight in self.edges:  # O(edge)
                if visited[src] and not visited[dest] and weight < min_edge[2]:
                    min_edge = [src, dest, weight]
            self.MST.append(min_edge)
            print(f"Visited: {min_edge[1]}")
            visited[min_edge[1]] = True
        self.display_solution()

    # NOTE: prefer this implementation because the concept of prims algorithm is to concentrate on vertices
    def prims_with_2d_array(self):  # O(vertex^3)
        visited = [0] * self.num_vertices
        num_edges = 0
        visited[0] = True
        while num_edges < self.num_vertices - 1:  # O(vertex)
            min = float("inf")
            for i in range(self.num_vertices):  # O(vertex)
                if visited[i]:
                    for j in range(self.num_vertices):  # O(vertex)
                        if not visited[j] and self.edges[i][j]:
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                src = i
                                dest = j
            self.MST.append([src, dest, min])
            visited[dest] = True
            num_edges += 1
        self.display_solution()


edges = [
    ["A", "B", 10],
    ["A", "C", 20],
    ["B", "A", 10],
    ["B", "C", 30],
    ["B", "D", 5],
    ["C", "A", 20],
    ["C", "B", 30],
    ["C", "D", 15],
    ["C", "E", 6],
    ["D", "B", 5],
    ["D", "C", 15],
    ["D", "E", 8],
    ["E", "C", 6],
    ["E", "D", 8],
]
nodes = ["A", "B", "C", "D", "E"]
graph = Graph(nodes, edges, nodes)
graph.prims()

# NOTE: other way to present edges 👇
# edges = [
#     # A, B, C, D, E <-to from
#     [0, 10, 20, 0, 0], # A
#     [10, 0, 30, 5, 0], # B
#     [20, 30, 0, 15, 6], # C
#     [0, 5, 15, 0, 8], # D
#     [0, 0, 6, 8, 0] # E
# ]

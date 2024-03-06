graph = {
    "A": ["B", "C"],
    "B": ["A", "E"],
    "C": ["A", "D"],
    "D": ["C", "E"],
    "E": ["B", "D"],
}


def display(graph):
    for vertex in graph:
        print(f"{vertex} -> {graph[vertex]}")


def BFS(graph, start):  # O(vertex + edge)
    visited = []
    queue = [start]
    while queue:  # O(vertex)
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            print(f"Visited: {visited}")
            for neighbor in graph[vertex]:  # O(edge)
                queue.append(neighbor)
    return visited


display(graph)
print(BFS(graph, "A"))  # ['A', 'B', 'C', 'E', 'D']

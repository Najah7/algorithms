graph = {
    "A": ["B", "C"],
    "B": ["A", "E"],
    "C": ["A", "D"],
    "D": ["C", "E"],
    "E": ["B", "D"]
}

def display(graph):
    for vertex in graph:
        print(f"{vertex} -> {graph[vertex]}")
        
def DFS(graph, start): # O(vertex + edge)
    visited = set()
    stack = [start]
    while stack: # O(vertex)
        current = stack.pop()
        if current not in visited:
            print(f"Visited: {current}")
            visited.add(current)
            for neighbor in graph[current]: # O(edge)
                stack.append(neighbor)
    
def recursive_DFS(graph, start, visited=None): # O(vertex + edge)
    if visited is None:
        visited = []
    if start not in visited: # O(vertex)
        visited.append(start)
        for neighbor in graph[start]: # O(edge)
            recursive_DFS(graph, neighbor, visited)
    return visited

display(graph)
print(DFS(graph, "A"))

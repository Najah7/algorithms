class Graph:
    
    def __init__(self, graph_dict=None) -> None:
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def bfs(self, start, goal): # O(vertex + edge)
        queue = []
        queue.append([start])
        while queue: # O(vertex)
            path = queue.pop(0)
            last_visited = path[-1]
            if last_visited == goal:
                return path
            for adjacent in self.graph_dict.get(last_visited, []): # O(edge)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                


graph_dict = {
    "A": ["B", "C"],
    "B": ["D", "G"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "G": ["F"],
}

graph = Graph(graph_dict)
print(graph.bfs("A", "F"))

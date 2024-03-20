import typing as t


class Graph:
    def __init__(self, gdict: t.Dict[str, t.List[str]] = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge) -> None:
        self.gdict[vertex].append(edge)

    def can_reach(self, src: str, dest: str) -> bool:
        visited = [src]
        queue = [src]
        path = False
        while queue:
            node = queue.pop(0)
            adjacencies = self.gdict[node]
            for adjacency in adjacencies:
                if adjacency not in visited:
                    if adjacency == dest:
                        path = True
                        break
                    else:
                        visited.append(node)
                        queue.append(adjacency)
        return path


gdict = {
    "a": ["c", "d", "b"],
    "b": ["j"],
    "c": ["g"],
    "d": [],
    "e": ["f", "a"],
    "f": ["i"],
    "g": ["d", "h"],
    "h": [],
    "i": [],
    "j": [],
}

graph = Graph(gdict=gdict)
result = graph.can_reach("a", "j")
print(result)

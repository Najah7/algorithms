import typing as t

sample_literal = t.Literal['A', 'B']
tmp: sample_literal = 'A'

class UnweightedUndirectedGraph:
    def __init__(self, graph_dict=None):
        self.adjacency_list: t.Dict[str, t.List[str]] = {}
        if graph_dict is None: # no graph_dict is provided
            self.adjacency_list = {}
        elif type(graph_dict) is dict: # usual case
            self.adjacency_list = graph_dict
        else: # invalid type for graph_dict
            raise TypeError('Invalid type for graph_dict')
    
    def add(self, vertex1, vertex2):
        # from vertex1 to vertex2
        if self.has_vertex(vertex1): self.adjacency_list[vertex1] = [vertex2]
        else: self.adjacency_list[vertex1] = [vertex2]
        # from vertex2 to vertex1
        if self.has_vertex(vertex2): self.adjacency_list[vertex2].append(vertex1)
        else: self.adjacency_list[vertex2] = [vertex1]
        
    def remove(self, vertex1, vertex2):
        # from vertex1 to vertex2
        if self.has_edge(vertex1, vertex2):
                self.adjacency_list[vertex1].remove(vertex2)
        # from vertex2 to vertex1
        if self.has_edge(vertex2, vertex1):
                self.adjacency_list[vertex2].remove(vertex1)
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def remove_vertex(self, target_vertex):
        if self.has_vertex(target_vertex):
            del self.adjacency_list[target_vertex]
            for from_vertex in self.adjacency_list: # O(n)
                if target_vertex in self.adjacency_list[from_vertex]: # O(1)
                    self.adjacency_list[from_vertex].remove(target_vertex)
    
    def bfs(self, start_vertex): # O(vertex + edge)
        visited = []
        queue = [start_vertex]
        while queue: # O(vertex)
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in self.adjacency_list[vertex]: # O(edge)
                    queue.append(neighbor)
        return visited

    def dfs(self, start_vertex): # O(vertex + edge)
        visited = []
        self._dfs(start_vertex, visited) # O(vertex + edge)
        return visited
    
    def _dfs(self, vertex, visited): # O(vertex + edge)
        if vertex not in visited: # O(vertex)
            visited.append(vertex)
            for neighbor in self.adjacency_list[vertex]: # O(edge)
                self._dfs(neighbor, visited)
    
    def has_vertex(self, vertex):
        return vertex in self.adjacency_list
    
    def has_edge(self, from_vertex, to_vertex):
        return from_vertex in self.adjacency_list and to_vertex in self.adjacency_list[from_vertex]
    
    
    
    def __str__(self) -> str:
        string = ''
        for vertex in self.adjacency_list:
            string += f'{vertex} -> {self.adjacency_list[vertex]}\n'
        return string
    
    
    
    
graph_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}

graph = UnweightedUndirectedGraph(graph_dict=graph_dict)
graph.add('A', 'D')
graph.add('G', 'H')
print(graph)
print(graph.dfs('A'))

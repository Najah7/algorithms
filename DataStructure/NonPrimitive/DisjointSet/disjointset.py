class DisjointSet:
    def __init__(self, vertices): # O(vertex)
        self.vertices = vertices
        self.parent = {}
        for v in vertices: # O(vertex)
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item): 
        if self.parent[item] == item:
            return item
        return self.find(self.parent[item])
    
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

vertices = ["A", "B", "C", "D", "E"]

disjoint_set = DisjointSet(vertices)
disjoint_set.union("A", "B")
print(disjoint_set.find("B"))

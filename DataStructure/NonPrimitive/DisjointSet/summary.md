## Disjoint Set (Union-Find) Data Structure
It's a data structure that keeps track of set of elements which are partitioned into a number of disjoint and non overlapping sets and each sets have representative which helps in identifying that sets.

## Use Cases
- **Cycle Detection**: It's used to detect cycle in a graph.
- **Kruskal's Algorithm**: It's used to find the minimum spanning tree in a graph.

## Operation of Disjoint Set
- **MakeSet(N)**: Create a set with N elements
- **Union(x, y)**: Merge two sets containing x and y
- **FindSet(x)**: Find the representative of the set containing x

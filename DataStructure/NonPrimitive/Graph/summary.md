# Graph

## Description
Graph consists of a finite set of vertices and a set of edges which connect a pair of vertices.

## Terminology of Graph
- **Vertex**: A vertex is a node in a graph.
- **Edge**: An edge is a link between two vertices.
- **Degree**: The degree of a vertex is the number of edges connected to it.
- **Path**: A path is a sequence of vertices connected by edges.
- **Cycle**: A cycle is a path that starts and ends at the same vertex.
- **Directed Graph**: A graph is directed if the edges have a direction.
- **Undirected Graph**: A graph is undirected if the edges do not have a direction.
- **Connected Graph**: A graph is connected if there is a path between every pair of vertices.
- **Weighted Graph**: A graph is weighted if the edges have a weight.
- **UnWeighted Graph**: A graph is unweighted if the edges do not have a weight.
- **Cycle Graph**: A graph that contains a cycle.
- **Acyclic Graph**: A graph that does not contain a cycle.
- **Tree**: It's a special case of directed acyclic graphs.

## Types of Graph
- Unweighted - undirected
- Unweighted - directed
- Positive - weighted - undirected
- Positive - weighted - directed
- Negative - weighted - undirected
- Negative - weighted - directed

## Graph Representation
- **Adjacency Matrix**: A 2D array of size V x V where V is the number of vertices in a graph.
    - when to use
        - when a graph is complete
    - Example
        ```
           A  B  C  D       
        A  0  1  0  1     [[0, 1, 0, 1],
        B  1  0  1  1  =>  [1, 0, 1, 1],
        C  0  1  0  1      [0, 1, 0, 1],
        D  1  1  1  0      [1, 1, 1, 0],]
        ```
- **Adjacency List**: A collection of linked lists or array that lists all the adjacent vertices of each vertex.
    - When to use
        - when the number of edges are fewer
    - Example
        ```
        Python Dict      LinkedList
        { 
          A: [B, D],     A -> B -> D
          B: [A, C, D],  B -> A -> C -> D
          C: [B, D],     C -> B -> D
          D: [A, B, C]   D -> A -> B -> C
        }
        ```

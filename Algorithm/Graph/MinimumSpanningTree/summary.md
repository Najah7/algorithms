# MinimumSpanningTree

## Description
A Minimum Spanning Tree (MST) is a subset of the edges of connected, weighted and undirected graph which: 
- Connects all the vertices together
- No Cycle
- Minimum total edge

## Kruskal's Algorithm
- It's a greedy algorithm.
- It finds a minimum spanning tree for a connected weighted graphs in two ways:
    - Add increasing cost edges at each step
    - Avoid any cycle at each step

## Prim's Algorithm
- It's a greedy algorithm.
- It finds a minimum spanning tree for weighted undirected graphs in following ways:
    1. Take any vertex as source set its weight to 0 and all other vertices to infinity.
    1. For every adjacent vertices if the current weight is more than current edge then we set it to current edge.
    1. Then we mark current vertex as visited
    1. Repeat these steps for all vertices in increasing order of weight.

## Kruskal's vs Prim's
- **Kruskal's Algorithm**
    - Concentrates on edges
    - Finalize edge in each iteration
- **Prim's Algorithm**
    - Concentrates on vertices
    - Finalize vertex in each iteration

## Applications
- **Kurskal's Algorithm**
    - Landing cable
    - TV Network
    - Tour Operation
    - LAN Network
    - A network of pipes for drinking water or natural gas
    - Single-link Cluster
- **Prim's Algorithm**
 - Network for roads and Rail tracks connecting all cities
 - Irrigation channels and placing microwave towers
 - Designing a fiber-optic grid or ICs
 - Traveling Salesman Problem
 - Cluster Analysis
 - Pathfinding algorithms used in AI

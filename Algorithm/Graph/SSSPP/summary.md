# Single Source Shortest Path Problem

## Description
finding a path between a given vertex (called source) to all other vertices in graph such that the total distance between them (source and destination) is minimum.

## Algorithms
- **Breadth First Search (BFS)**
    - It works for both directed and undirected graphs.
    - It doesn't work for weighted graphs.
    - It uses a queue to keep track of the vertices to visit.
    - It's time complexity is O(V + E).
- **Dijkstra's Algorithm**
    - It works for both directed and undirected graphs.
    - It works for weighted graphs.
    - It doesn't work with negative cycles.
    - It uses a priority queue to keep track of the vertices to visit.
    - It's a greedy algorithm.
    - It's time complexity is O(V^2) for an adjacency matrix and O(E + VlogV) for an adjacency list.
- **Bellman-Ford Algorithm**
    - It works for both directed and undirected graphs.
    - It works for both positive and negative weighted graphs.
    - It uses a queue to keep track of the vertices to visit.
    - It's a dynamic programming algorithm. (memorized each iteration)
    - iterates through all the edges V-1 times to find the shortest path.


## Why does DFS not work with SSSPP?
DFS has the tendency to go "as far as possible" from source, hence it can never find "Shortest Path"

## Table for comparison

### Possible Combinations
| Graph Type | BFS | Dijkstra's Algorithm | Bellman-Ford Algorithm |
| --- | --- | --- | --- |
| Unweighted - undirected | ✔️ | ✔️ | ✔️ |
| Unweighted - directed | ✔️ | ✔️ | ✔️ |
| Positive - weighted - undirected | ❌ | ✔️ | ✔️ |
| Positive - weighted - directed | ❌ | ✔️ | ✔️ |
| Negative - weighted - undirected | ❌ | ✔️ | ✔️ |
| Negative - weighted - directed | ❌ | ✔️ | ✔️ |
| Negative Cycle | ❌ | ❌ | ✔️ |

### Complexity
|  | BFS | Dijkstra's Algorithm | Bellman-Ford Algorithm |
| --- | --- | --- | --- |
| Time Complexity | O(V^2) | O(V^2) | O(VE) |
| Space Complexity | O(E) | O(V) | O(V) |
| Implementation | Easy | Moderate | Moderate |
| Limitation | Doesn't work for weighted graphs | Doesn't work with negative cycles | N/A |
| Unweighted Graph | 👍 (time is better and easy to implement) | 🙅 (not easy to implement) | 🙅(not easy to implement) |
| Weighted Graph | 🙅 (not supported) | 👍 (time is better than bellman) | 👍 (time is worse than dijkstra) |
| Negative Weighted Graph | 🙅 (not supported) | 🙅 (not supported) | 👍 (supported) |

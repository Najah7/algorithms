# All Pair Shortest Path (APSP) Problem
finding a path between every vertex to all other vertices in a graph such that the total distance between them (source and destination) is minimum.

## Algorithms
- **Floyd-Warshall Algorithm**
    - It works for both directed and undirected graphs.
    - It doesn't work for negative cycles.
    - It uses a 2D array to keep track of the vertices to visit.
    - It's a dynamic programming algorithm. (memorized each iteration)
    - iterates through all the vertices to find the shortest path. (V times) <- first-> initial, second-> via V1, third-> via V2, ... via Vn

## Table for comparison

| | BFS | Dijkstra's Algorithm | Bellman-Ford Algorithm | Floyd-Warshall Algorithm |
| --- | --- | --- | --- | --- |
| Time Complexity | O(V^3) | O(V^3) | O(VE^2) | O(V^3) |
| Space Complexity | O(EV) | O(EV) | O(V^2) | O(V^2) |
| Implementation | Easy | Moderate | Moderate | Moderate |
| Limitation | Doesn't work for weighted graphs | Doesn't work with negative cycles | N/A | Doesn't work with negative cycles |
| Unweighted Graph | 👍 (time is better and easy to implement) | 🙅 (not easy to implement) | 🙅(not easy to implement) | 👍(can be used) |
| Weighted Graph | 🙅 (not supported) | 👍 (can be used) | 🙅 (not use as time complexity is bad) | 👍(can be preferred as implementation easy) |
| Negative Weighted Graph | 🙅 (not supported) | 🙅 (not supported) | 👍 (use this as other not support) | 🙅 (not supported) |

import typing as t

def display_solution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == float("inf"):
                print("inf", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")

# graph int list or float list
def floyd_warshall(
        graph: t.Union[t.List[t.List[int]],t.List[t.List[float]]],
        nV: int) -> None: # O(vertex^3)
    distance = graph
    # NOTE: we create multiple memos by each via vertex
    for via in range(nV): # O(vertex)
        # NOTE: creating one of the memos
        for src in range(nV): # O(vertex)
            for dest in range(nV): # O(vertex)
                try:
                    distance[src][dest] = min(distance[src][dest], distance[src][via] + distance[via][dest])
                except TypeError:
                    print(distance)

    display_solution(nV, distance)

graph = [
    [0, 8, float("inf"), 1],
    [float("inf"), 0, 1, float("inf")],
    [4, float("inf"), 0, float("inf")],
    [float("inf"), 2, 9, 1]
]

floyd_warshall(graph, 4)

from waypoint.preprocessing import file_to_graph, file_to_airports
from waypoint.algorithms import djikstra, bfs


def main():
    graph = file_to_graph("../data/data.csv")
    airports = file_to_airports("../data/airports.csv")

    # Example: Find path from BOS to MCO
    path = djikstra(graph, 10721, 11953)
    print("Djikstra Path from BOS to MCO:")
    if path.flights is None:
        print("No path found")
        return
    for airport_id in path.flights:
        print(airports[airport_id])
    print(path.time)

    path = bfs(graph, 10721, 11953)
    print("BFS Path from BOS to MCO:")
    if path.flights is None:
        print("No path found")
        return
    for airport_id in path.flights:
        print(airports[airport_id])
    print(path.time)


if __name__ == "__main__":
    main()

from waypoint.preprocessing import file_to_graph, file_to_airports
from waypoint.algorithms import djikstra, bfs, a_star

from pprint import pprint


def main():
    graph = file_to_graph("../data/data.csv")
    airports = file_to_airports("../data/airports.csv")

    path = djikstra(graph, 10721, 11953)
    if path.flights is None:
        print("No path found")
        return
    for airport_id in path.flights:
        print(airports[airport_id])


if __name__ == "__main__":
    main()

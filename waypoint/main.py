from preprocessing import file_to_graph, file_to_airports
from algorithms import djikstra, bfs, a_star

from pprint import pprint


def main():
    graph = file_to_graph("../data/data.csv")
    # pprint(graph)
    # airports = file_to_airports("../data/airports.csv")
    # pprint(airports)
    # djikstra(graph, 10000, 10001)
    # bfs(graph, 10000, 10001)
    # a_star(graph, 10000, 10001)


if __name__ == "__main__":
    main()

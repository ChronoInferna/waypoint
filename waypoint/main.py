from preprocessing import file_to_graph, file_to_airports
from algorithms import djikstra, bfs, a_star

from pprint import pprint


def main():
    pprint(file_to_graph("../data/data.csv"))
    graph = file_to_graph("../data/data.csv")
    airports = file_to_airports("../data/airports.csv")
    # djikstra.djikstra(graph)
    # bfs.bfs(graph)
    # a_star.a_star(graph)


if __name__ == "__main__":
    main()

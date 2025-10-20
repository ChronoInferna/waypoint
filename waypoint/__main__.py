from preprocessing import file_to_graph
from algorithms.djikstra import djikstra
from algorithms.bfs import bfs

from pprint import pprint


def main():
    pprint(file_to_graph("../data/data.csv"))
    graph = file_to_graph("../data/data.csv")
    # djikstra(graph)
    # bfs(graph)


if __name__ == "__main__":
    main()

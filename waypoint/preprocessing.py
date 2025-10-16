import csv


def convert_to_graph(file_path):
    graph = {}
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            # We want ORIGIN_AIRPORT_ID, DEST_AIRPORT_ID and ACTUAL ELAPSED TIME
            origin, dest, time = row[5], row[8], row[11]
            if origin not in graph:
                graph[origin] = []
            graph[dest].append((origin, int(time)))
    return graph

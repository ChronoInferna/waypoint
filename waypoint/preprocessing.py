import csv


def file_to_graph(file_path) -> dict[int, list[tuple[int, float]]]:
    graph = {}
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            origin, dest, time = (
                row["ORIGIN_AIRPORT_ID"],
                row["DEST_AIRPORT_ID"],
                row["ACTUAL_ELAPSED_TIME"],
            )
            if origin not in graph:
                graph[origin] = []
            graph[origin].append((dest, time))
    return graph

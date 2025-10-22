import csv


def file_to_graph(file_path) -> dict[int, list[tuple[int, float]]]:
    """Parses a CSV file containing flight data and returns a graph representation as an adjacency list."""
    graph = {}
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            origin, dest, time = (
                row["ORIGIN_AIRPORT_ID"],
                row["DEST_AIRPORT_ID"],
                row["ACTUAL_ELAPSED_TIME"],
            )
            if not origin or not dest or not time:
                continue
            if origin not in graph:
                graph[origin] = []
            graph[origin].append((dest, time))
    return graph


def file_to_airports(file_path) -> dict[int, str]:
    """Parses a CSV file containing airport data and returns a dictionary mapping airport IDs to airport names."""
    airports = {}
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            airport_id, airport_name = row["AIRPORT_ID"], row["AIRPORT_NAME"]
            if airport_id and airport_name:
                airports[airport_id] = airport_name
    return airports

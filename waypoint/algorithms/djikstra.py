from waypoint.path import Path


def djikstra(graph: dict[int, dict[int, float]], start: int, destination: int) -> Path:

    unvisited = {
        n: float("inf") for n in graph
    }  # Dict of unvisited nodes, all with infinite weight
    # Probably not best practice to raise KeyError here instead of returning Path with None flights but it's too late to change now
    if start not in graph.keys():
        return Path(flights=None, time=float("inf"))
    unvisited[start] = 0  # Start node given weight of 0
    visited = {}
    previous = {}

    while unvisited:
        minimum = min(unvisited, key=unvisited.get)  # Start from lowest weight
        current_distance = unvisited[minimum]

        for neighbor, weight in graph.get(
            minimum, {}
        ).items():  # Start from lowest weight
            if neighbor in visited:
                continue

            distance = current_distance + weight
            if distance < unvisited.get(neighbor, float("inf")):
                unvisited[neighbor] = distance  # Assign total distance to next node
                previous[neighbor] = minimum  # Assign last node to be predecessor

        visited[minimum] = (
            current_distance  # Last node is assigned the total distance traveled
        )
        unvisited.pop(minimum)

    # Path starts at destination and iterates through predecessors
    path = [destination]
    while path[-1] != start:
        if path[-1] not in previous:
            return Path(flights=None, time=float("inf"))
        path.append(previous[path[-1]])
    path.reverse()  # Reverse list so path is start location to end location

    return Path(flights=path, time=visited[destination])

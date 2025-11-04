from waypoint.path import Path


def bfs(graph: dict[int, dict[int, float]], start: int, destination: int) -> Path:
    visited: set[int] = set()
    queue: list[tuple[int, float, list[int]]] = [(start, 0, [])]

    while queue:
        current, time, path = queue.pop(0)
        current: int
        time: float
        path: list[int]

        if current == destination:
            return Path.from_list(path + [current], time)

        if current not in visited:
            visited.add(current)
            neighbors = graph.get(current, {})
            for neighbor, weight in neighbors.items():
                if neighbor not in visited:
                    queue.append((neighbor, time + weight, path + [current]))

    return Path.empty()

from dataclasses import dataclass


@dataclass
class Path:
    flights: dict[int, int]
    distance: float

from dataclasses import dataclass


@dataclass
class Path:
    flights: list[int]
    distance: float

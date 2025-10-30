from dataclasses import dataclass


@dataclass
class Path:
    flights: list[int] | None
    distance: float

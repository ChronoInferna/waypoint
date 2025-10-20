from dataclasses import dataclass


@dataclass
class Path:
    flights: dict[str, str]
    distance: float

from dataclasses import dataclass


@dataclass
class Path:
    _flights: list[int] | None
    _time: float

    @classmethod
    def empty(cls) -> "Path":
        """Creates an empty path with no flights and infinite time."""
        return cls(_flights=None, _time=float("inf"))

    @classmethod
    def from_list(cls, flights: list[int], time: float = 0.0) -> "Path":
        """Creates a path from a list of flights and an optional time."""
        if time < 0:
            raise ValueError("Time must be non-negative")
        return cls(_flights=flights, _time=time)

    def __post_init__(self):
        if self._flights is None:
            self._time = float("inf")
        elif self._time < 0:
            raise ValueError("Time must be non-negative")

    @property
    def flights(self) -> list[int] | None:
        return self._flights

    @flights.setter
    def flights(self, value: list[int] | None):
        self._flights = value
        if value is None:
            self._time = float("inf")

    @property
    def time(self) -> float:
        return self._time

    @time.setter
    def time(self, value: float):
        if value != float("inf") and value < 0:
            raise ValueError("Time must be non-negative")
        self._time = value

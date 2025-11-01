from dataclasses import dataclass


@dataclass
class Path:
    """
    Represents a path consisting of a sequence of flights and the total time taken.
    Attributes:
        flights (list[int] | None): A list of flight IDs representing the path. None indicates no path.
        time (float): The total time taken for the path. Infinite time indicates no path.
    """

    _flights: list[int] | None
    _time: float

    # Initialization is restricted to factory methods only
    def __new__(cls, *args: object, **kwargs: object):
        raise TypeError(
            "Direct instantiation is not allowed. Use class methods to create instances."
        )

    @classmethod
    def empty(cls) -> "Path":
        """Creates an empty path with no flights and infinite time."""
        self = super().__new__(cls)
        self._flights = None
        self._time = float("inf")
        return self

    @classmethod
    def from_list(cls, flights: list[int] | None, time: float = 0.0) -> "Path":
        """Creates a path from a list of flights and an optional time."""
        self = super().__new__(cls)
        self._flights = flights
        self._time = time

        # Invariant checks
        if flights is None:
            self._time = float("inf")

        if self._time < 0:
            raise ValueError("Time must be non-negative")
        elif self._time == float("inf"):
            self._flights = None

        return self

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
        if value == float("inf"):
            self._flights = None
        if value < 0:
            raise ValueError("Time must be non-negative")
        self._time = value

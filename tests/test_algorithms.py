import pytest
from waypoint.algorithms import bfs, djikstra, a_star
from waypoint.path import Path


@pytest.fixture
def simple_graph():
    return {
        100: {200: 1.0, 300: 4.0},
        200: {300: 2.0, 400: 5.0},
        300: {400: 1.0},
        400: {},
    }


@pytest.fixture
def no_path_graph():
    return {
        100: {200: 1.0},
        200: {},
        300: {400: 1.0},
        400: {},
    }


@pytest.fixture
def cyclic_graph():
    return {
        100: {200: 1.0, 300: 2.0},
        200: {300: 3.0, 100: 1.0},
        300: {100: 2.0, 400: 4.0},
        400: {},
    }


@pytest.fixture
def multiple_paths_graph():
    return {
        100: {200: 1.0, 300: 2.0},
        200: {400: 5.0},
        300: {400: 2.0},
        400: {},
    }


# Parameterize tests for each algorithm
algorithm_parametrize = pytest.mark.parametrize(
    "algorithm",
    [
        pytest.param(bfs, marks=pytest.mark.xfail(reason="BFS not implemented")),
        pytest.param(
            djikstra,
            # marks=pytest.mark.xfail(reason="Dijkstra not implemented"),
        ),
        pytest.param(a_star, marks=pytest.mark.xfail(reason="A* not implemented")),
    ],
)


# Tests
@algorithm_parametrize
class TestAlgorithms:
    def test_simple_path(self, algorithm, simple_graph):
        result = algorithm(simple_graph, 100, 400)
        assert isinstance(result, Path)
        assert result.flights == [100, 200, 300, 400]
        assert result.time == 4

    def test_no_path_exists(self, algorithm, no_path_graph):
        result = algorithm(no_path_graph, 100, 400)
        assert result.flights is None
        assert result.time == float("inf")

    def test_cyclic_path(self, algorithm, cyclic_graph):
        result = algorithm(cyclic_graph, 100, 400)
        assert result.flights is not None
        assert result.flights[-1] == 400
        assert result.time <= 7  # Maximum possible path length

    def test_multiple_paths(self, algorithm, multiple_paths_graph):
        result = algorithm(multiple_paths_graph, 100, 400)
        assert result.flights == [100, 300, 400]  # Should find shortest path
        assert result.time == 4

    def test_same_start_end(self, algorithm, simple_graph):
        result = algorithm(simple_graph, 100, 100)
        assert result.flights == [100]
        assert result.time == 0

    def test_nonexistent_start(self, algorithm, simple_graph):
        with pytest.raises(KeyError):
            algorithm(simple_graph, 999, 400)

    def test_nonexistent_end(self, algorithm, simple_graph):
        result = algorithm(simple_graph, 100, 999)
        assert result.flights is None
        assert result.time == float("inf")


# Edge Cases
@algorithm_parametrize
class TestEdgeCases:
    def test_empty_graph(self, algorithm):
        with pytest.raises(KeyError):
            algorithm({}, 100, 400)

    @pytest.mark.parametrize(
        "invalid_graph",
        [
            None,
            "not a graph",
            123,
            [],
        ],
    )
    def test_invalid_graph_type(self, algorithm, invalid_graph):
        with pytest.raises((TypeError, AttributeError)):
            algorithm(invalid_graph, 100, 400)

    def test_negative_weights(self, algorithm):
        negative_graph = {
            100: {200: -1},
            200: {300: -2},
            300: {},
        }
        result = algorithm(negative_graph, 100, 300)
        assert result.flights is not None
        assert result.flights == [100, 200, 300]
        assert result.time == -3


# Performance Tests
@algorithm_parametrize
class TestPerformance:
    @pytest.fixture
    def large_graph(self):
        # Create a large graph with 1000 nodes
        return {i: {(i + 1): 1} if i < 1000 else {} for i in range(100, 1101)}

    def test_large_graph_performance(self, algorithm, large_graph):
        result = algorithm(large_graph, 100, 1000)
        assert result.flights is not None
        assert len(result.flights) == 901  # Path from 100 to 1000
        assert result.time == 900  # 900 edges with weight 1

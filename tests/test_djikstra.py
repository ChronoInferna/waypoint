import pytest

from waypoint.algorithms.djikstra import djikstra


@pytest.mark.xfail(reason="Djikstra algorithm not yet implemented")
def test_djikstra():
    graph = {
        100: {"200": 1, "300": 4},
        200: {"300": 2, "400": 5},
        300: {"400": 1},
        400: {},
    }
    start = 100
    end = 400
    expected_path = [100, 200, 300, 400]
    expected_cost = 4

    res = djikstra(graph, start, end)

    assert (
        res.flights == expected_path
    ), f"Expected path {expected_path}, but got {res.flights}"
    assert (
        res.distance == expected_cost
    ), f"Expected cost {expected_cost}, but got {res.distance}"


@pytest.mark.xfail(reason="Djikstra algorithm not yet implemented")
def test_djikstra_no_path():
    graph = {
        100: {"200": 1},
        200: {},
        300: {"400": 1},
        400: {},
    }
    start = 100
    end = 400

    res = djikstra(graph, start, end)

    assert res.flights is None, f"Expected no path, but got {res.flights}"
    assert res.distance == float(
        "inf"
    ), f"Expected infinite cost, but got {res.distance}"

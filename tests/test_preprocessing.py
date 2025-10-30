import pytest
import tempfile
import os
import csv
from waypoint.preprocessing import file_to_graph, file_to_airports


@pytest.fixture
def temp_csv():
    """Fixture to create and clean up a temporary CSV file."""
    files = []

    def _create_temp_csv(headers, rows):
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", newline="")
        files.append(temp_file.name)
        with temp_file as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
        return temp_file.name

    yield _create_temp_csv

    for file in files:
        os.unlink(file)


# Tests for file_to_graph
@pytest.mark.parametrize(
    "headers,rows,expected",
    [
        # Valid input
        (
            ["ORIGIN_AIRPORT_ID", "DEST_AIRPORT_ID", "ACTUAL_ELAPSED_TIME"],
            [
                ["100", "200", "50"],
                ["200", "300", "30"],
                ["100", "300", "70"],
            ],
            {100: {200: 50.0, 300: 70.0}, 200: {300: 30.0}},
        ),
        # Empty file
        (
            ["ORIGIN_AIRPORT_ID", "DEST_AIRPORT_ID", "ACTUAL_ELAPSED_TIME"],
            [],
            {},
        ),
        # Missing columns
        (
            ["ORIGIN_AIRPORT_ID", "DEST_AIRPORT_ID"],
            [["100", "200"]],
            KeyError,
        ),
        # Invalid data
        (
            ["ORIGIN_AIRPORT_ID", "DEST_AIRPORT_ID", "ACTUAL_ELAPSED_TIME"],
            [["100", "", "50"], ["", "300", "30"]],
            {},
        ),
    ],
)
def test_file_to_graph(headers, rows, expected, temp_csv):
    file_path = temp_csv(headers, rows)
    if isinstance(expected, dict):
        assert file_to_graph(file_path) == expected
    else:
        with pytest.raises(expected):
            file_to_graph(file_path)


# Tests for file_to_airports
@pytest.mark.parametrize(
    "headers,rows,expected",
    [
        # Valid input
        (
            ["AIRPORT_ID", "AIRPORT_NAME"],
            [["100", "Airport A"], ["200", "Airport B"]],
            {100: "Airport A", 200: "Airport B"},
        ),
        # Empty file
        (
            ["AIRPORT_ID", "AIRPORT_NAME"],
            [],
            {},
        ),
        # Missing columns
        (
            ["AIRPORT_ID"],
            [["100"]],
            KeyError,
        ),
        # Invalid data
        (
            ["AIRPORT_ID", "AIRPORT_NAME"],
            [["", "Airport A"], ["200", ""]],
            {},
        ),
    ],
)
def test_file_to_airports(headers, rows, expected, temp_csv):
    file_path = temp_csv(headers, rows)
    if isinstance(expected, dict):
        assert file_to_airports(file_path) == expected
    else:
        with pytest.raises(expected):
            file_to_airports(file_path)

import csv
import waypoint.preprocessing as preprocessing


def test_convert_to_graph(tmp_path):
    file_path = tmp_path / "flights.csv"
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["ORIGIN_AIRPORT_ID", "DEST_AIRPORT_ID", "ACTUAL_ELAPSED_TIME"],
        )
        writer.writeheader()
        writer.writerow(
            {
                "ORIGIN_AIRPORT_ID": "A",
                "DEST_AIRPORT_ID": "B",
                "ACTUAL_ELAPSED_TIME": "100",
            }
        )
        writer.writerow(
            {
                "ORIGIN_AIRPORT_ID": "A",
                "DEST_AIRPORT_ID": "C",
                "ACTUAL_ELAPSED_TIME": "200",
            }
        )
        writer.writerow(
            {
                "ORIGIN_AIRPORT_ID": "B",
                "DEST_AIRPORT_ID": "C",
                "ACTUAL_ELAPSED_TIME": "150",
            }
        )

    graph = preprocessing.file_to_graph(file_path)

    expected = {
        "A": [("B", "100"), ("C", "200")],
        "B": [("C", "150")],
    }

    assert graph == expected


def test_convert_to_graph_empty_file(tmp_path):
    file_path = tmp_path / "empty_flights.csv"
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["ORIGIN_AIRPORT_ID", "DEST_AIRPORT_ID", "ACTUAL_ELAPSED_TIME"],
        )
        writer.writeheader()

    graph = preprocessing.file_to_graph(file_path)

    expected = {}

    assert graph == expected

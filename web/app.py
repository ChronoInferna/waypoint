from typing import cast, TypedDict

from flask import Flask, render_template, request, jsonify

from waypoint.preprocessing import file_to_graph, file_to_airports
from waypoint.algorithms import djikstra
from waypoint.path import Path

app = Flask(__name__)

_ = app.config.from_pyfile("config.py")

data_path = cast(str, app.config["DATA_PATH"])
graph: dict[int, dict[int, float]] = file_to_graph(data_path)

airports_path = cast(str, app.config["AIRPORTS_PATH"])
airports: dict[int, str] = file_to_airports(airports_path)


class RequestData(TypedDict):
    start: int
    end: int


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    data: RequestData = cast(RequestData, request.get_json())
    start = int(data["start"])
    end = int(data["end"])

    path = djikstra(graph, start, end)

    if path == Path.empty():
        return jsonify({"message": "No path found."})

    return jsonify(
        {
            "flights": (
                [airports[airport_id] for airport_id in path.flights]
                if path.flights is not None
                else []
            ),
            "time": path.time,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)

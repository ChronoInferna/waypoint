from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    start = data["start"]
    end = data["end"]

    # find dest using djikstra or bfs

    message = f"Fastest route calculated from {start} to {end}"
    return jsonify({
        "message": message
    })

if __name__ == '__main__':
    app.run(debug=True)

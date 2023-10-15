from flask import Flask, request, jsonify
from pathlib import Path
import json
from flask_cors import CORS, cross_origin

import sys

sys.path.insert(0, ".")
from matching_loop import do_conversations_for_human

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

base_path = Path(__file__).parent

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user_input", methods=["POST"])
@cross_origin(origin="localhost", headers=["Content-Type"])
def store_text():
    data = request.get_json()
    name = data["name"]
    with open(base_path / "data" / "db" / "people" / f"{name}.json", "a") as file:
        json.dump(data, file)
    response = jsonify({"data": "Success!"})
    return response


@app.route("/run_convos", methods=["POST"])
@cross_origin(origin="localhost", headers=["Content-Type"])
def store_text():
    data = request.get_json()
    name = data["name"]
    top_compatibility = do_conversations_for_human(name)
    score, name, compatibility = top_compatibility
    response = jsonify({"data": top_compatibility})

    return response

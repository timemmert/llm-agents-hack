from flask import Flask, request, jsonify
import os
from pathlib import Path
import json
from flask_cors import CORS, cross_origin
from backend.matching_loop import do_conversations_for_human

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
    with open(base_path / "data" / "db" / "people" / f"{name}.txt", "a") as file:
        file.write(f"{data['info']}\n")
    response = jsonify({"data": "Success!"})
    return response


@app.route("/run_matching", methods=["POST"])
@cross_origin(origin="localhost", headers=["Content-Type"])
def run_matching():
    name = request.get_json()["name"]
    print(name)
    scores = do_conversations_for_human(name)
    return jsonify(scores)

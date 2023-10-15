from flask import Flask, request
import os
from pathlib import Path
import json

app = Flask(__name__)

base_path = Path(__file__).parent

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user_input", methods=["POST"])
def store_text():
    data = request.get_json()
    name = data["name"]
    with open(base_path / "data" / "db" / "people" / f"{name}.json", "a") as file:
        json.dump(data, file)
    return {"response": "Information stored successfully!"}

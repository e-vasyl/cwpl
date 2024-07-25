from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(time=datetime.now())

#!/usr/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 35, "city": "New York"}
}

@app.route("/data")
def get_user():

    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)

#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample users data
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Home route
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to return all usernames
@app.route("/data", methods=["GET"])
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)

# Status endpoint
@app.route("/status", methods=["GET"])
def get_status():
    return "OK"

# Route to get details of a specific user by username
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user via POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Check if username is provided
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Check if user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add new user to the dictionary
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)

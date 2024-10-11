#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route for serving JSON data with the list of usernames
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# Route for checking status
@app.route('/status')
def status():
    return "OK"

# Route for getting a specific user's data by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route for adding a new user (POST request)
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Check if username is provided
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    # Check for duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Add the new user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    # Return confirmation message with the added user's data
    return jsonify({
        "message": "User added",
        "user": users[username]
    })

if __name__ == "__main__":
    app.run(debug=True)

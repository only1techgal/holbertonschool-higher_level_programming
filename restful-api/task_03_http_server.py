#!/usr/bin/python3

import http.server
import socketserver
import json

# Set the port for the server
PORT = 8000

# Create a subclass of BaseHTTPRequestHandler to handle HTTP requests
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Root endpoint ("/") - Return a simple message
        if self.path == "/":
            self.send_response(200)  # OK status
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        # /data endpoint - Return a sample JSON dataset
        elif self.path == "/data":
            self.send_response(200)  # OK status
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(sample_data).encode())
        
        # /status endpoint - Return OK status
        elif self.path == "/status":
            self.send_response(200)  # OK status
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        
        # /info endpoint - Return API version and description
        elif self.path == "/info":
            self.send_response(200)  # OK status
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_data).encode())
        
        # Undefined endpoint - Return a 404 status
        else:
            self.send_response(404)  # Not Found status
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_data = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_data).encode())

# Set up the server with the specified port and request handler
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

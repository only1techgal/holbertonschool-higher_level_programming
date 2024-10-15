#!/usr/bin/python3

import http.server
import json
from http import HTTPStatus

class SimpleAPHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text5/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(HTTPStatus.OK)
            self.end_headers("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode("utf-8"))


        elif self.path == "/status":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode("utf-8"))


        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode("utf-8"))

if __name__ == "__main__":

    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()

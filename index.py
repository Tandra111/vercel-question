import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

with open("marks.json", "r") as f:
    marks_data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        query_components = parse_qs(urlparse(self.path).query)
        names = query_components.get("name", [])

        result = [marks_data.get(name, None) for name in names]

        response = json.dumps({"marks": result})
        self.wfile.write(response.encode())

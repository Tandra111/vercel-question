import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Parse query parameters
        query_components = parse_qs(urlparse(self.path).query)
        names = query_components.get("name", [])

        # Load data from marks.json
        filepath = os.path.join(os.getcwd(), "marks.json")
        with open(filepath, "r") as file:
            data = json.load(file)

        # Build name-to-marks mapping
        marks_map = {entry["name"]: entry["marks"] for entry in data}
        result = [marks_map.get(name, None) for name in names]

        # Return the result as JSON
        self.wfile.write(json.dumps({"marks": result}).encode())

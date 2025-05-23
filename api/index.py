import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import os

# Load and convert list to dict
json_path = os.path.join(os.path.dirname(__file__), '..', 'marks.json')
with open(json_path, 'r') as f:
    raw_data = json.load(f)
    marks_data = {entry["name"]: entry["marks"] for entry in raw_data}

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

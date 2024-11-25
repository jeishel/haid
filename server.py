import http.server
import socketserver

# Define the port for the server
PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    # Overriding to serve from the current directory
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)

# Create the server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

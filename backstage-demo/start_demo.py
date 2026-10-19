import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print("=" * 60)
print("  🚀 LANCEMENT DE LA DÉMONSTRATION SPOTIFY BACKSTAGE IDP")
print("=" * 60)
print(f"Serveur local démarré sur : http://localhost:{PORT}")
print("Appuyez sur Ctrl+C dans ce terminal pour arrêter le serveur.")
print("=" * 60)

webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur Backstage Démo.")
        sys.exit(0)

from http.server import SimpleHTTPRequestHandler, HTTPServer

class MiManejador(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Soy Colombiano</title>
                <style>
                    body {
                        background: linear-gradient(to bottom, #FFD700 33%, #0033A0 33%, #0033A0 66%, #D52B1E 66%);
                        background-size: 100% 300%;
                        background-position: 0 0;
                        color: white;
                        text-align: center;
                        font-family: Arial, sans-serif;
                        margin-top: 100px;
                    }
                    h1 {
                        font-size: 50px;
                        text-shadow: 2px 2px 5px black;
                    }
                    button {
                        padding: 15px 30px;
                        font-size: 18px;
                        background-color: red;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        cursor: pointer;
                        box-shadow: 2px 2px 8px black;
                        margin: 10px;
                    }
                </style>
            </head>
            <body>
                <h1>Soy Colombiano</h1>
                <button id="toggleButton" onclick="toggleMusic()">▶ Reproducir canción</button>
                <button id="loopButton" onclick="toggleLoop()">🔁 Loop: OFF</button>
                <audio id="musica" src="soy_colombiano.mp3"></audio>

                <script>
                    var musica = document.getElementById('musica');
                    var toggleButton = document.getElementById('toggleButton');
                    var loopButton = document.getElementById('loopButton');

                    function toggleMusic() {
                        if (musica.paused) {
                            musica.play();
                            toggleButton.innerHTML = '⏸ Pausar canción';
                        } else {
                            musica.pause();
                            toggleButton.innerHTML = '▶ Reproducir canción';
                        }
                    }

                    function toggleLoop() {
                        musica.loop = !musica.loop;
                        loopButton.innerHTML = musica.loop ? '🔁 Loop: ON' : '🔁 Loop: OFF';
                    }
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

if __name__ == '__main__':
    puerto = 8000
    servidor = HTTPServer(('localhost', puerto), MiManejador)
    print(f"Servidor corriendo en http://localhost:{puerto}")
    servidor.serve_forever()


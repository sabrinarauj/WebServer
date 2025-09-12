from http.server import SimpleHTTPRequestHandler, HTTPServer

# # definindo a porta do servidor
# port = 8000

# # definindo o gerenciador/manipulador de requisições
# handler = SimpleHTTPRequestHandler

# # criando a instancia do servidor
# server = HTTPServer(('localhost', port), handler)

# # imprimindo mensagem de ok
# print(f"Server running in http://localhost:{port}")
# server.serve_forever()

import os
from http.server import SimpleHTTPRequestHandler

class MyHandle(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            f = open(os.path.join(path, 'index.html'), 'r')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass
        return super().list_directory(path)
    
    def do_GET(self):
        if self.path == "/login":
            try:
                with open(os.path.join(os.getcwd(), 'login.html'), 'r') as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type: ", "text/html")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
        else:
            super().do_GET()

    def do_GET(self):
        if self.path == "/cadastro":
            try:
                with open(os.path.join(os.getcwd(), 'cadastro.html'), 'r') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type ", "text/html")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
        else:
            super().do_GET()

    def do_GET(self):
        if self.path == "/filmes":
            try:
                with open(os.path.join(os.getcwd(), 'filmes.html'), encoding='utf-8') as filmes:
                    content = filmes.read()
                self.send_response(200)
                self.send_header("Content-type ", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
        else:
            super().do_GET()


def main():
    server_address = ('',8001)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server running in http://localhost:8001")
    httpd.serve_forever()

main()
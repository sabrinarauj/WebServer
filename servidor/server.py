# importando as bibliotecas do http
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

# cria uma classe MyHandle que herda de SimpleHTTPRequestHandler
class MyHandle(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            # acessa o arquivo index.html e manda uma resposta HTTP ao cliente
            f = open(os.path.join(path, 'index.html'),'r')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass
        # caso não haja o arquivo index.html retorna a lista de diretórios
        return super().list_directory(path)
    
    # sobrescreve o método GET e verifica se o caminho requisitado é /login
    def do_GET(self):
        if self.path == "/login":
            try:
                # tenta abrir o arquivo login.html no diretório atual do servidor
                with open(os.path.join(os.getcwd(), 'login.html'), 'encoding=utf-8') as login:
                    content = login.read()
                # manda uma resposta HTTP
                self.send_response(200)
                # cabeçalho da resposta com o tipo de contéudo (html)
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
                with open(os.path.join(os.getcwd(), 'cadastro.html'), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type ", "text/html")
                self.end_headers()
                # garante que não haja erros de acentuação
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
                # exception caso o caminho do arquivo não seja encontrado
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
        else:
            super().do_GET()

# a main roda o servidor e chama a classe MyHandle
# cria um caminho localhost e define a porta que irá rodar o servidor
def main():
    server_address = ('',8001)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server running in http://localhost:8001")
    httpd.serve_forever()

main()
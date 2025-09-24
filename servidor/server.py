# importando as bibliotecas do http
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# cria uma classe MyHandle que herda de SimpleHTTPRequestHandler
class MyHandle(SimpleHTTPRequestHandler):

    def list_directory(self, path):
        try:
            f = open(os.path.join(path, 'index.html'), encoding='utf-8')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass
        return super().list_directory(path)
    
    def accont_user(self, login, password):
        loga = "sabrina@gmail.com"
        senha = "123456"
        if login == loga and senha == password:
            return "Usuário logado"
        else:
            return "Usuário não existe"
    
    # sobrescreve o método GET
    def do_GET(self):
        if self.path == "/login":
            try:
                with open(os.path.join(os.getcwd(), 'login.html'), encoding='utf-8') as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/cadastro":
            try:
                with open(os.path.join(os.getcwd(), 'cadastro.html'), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/filmes":
            try:
                with open(os.path.join(os.getcwd(), 'filmes.html'), encoding='utf-8') as filmes:
                    content = filmes.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
        else:
            super().do_GET()

    # sobrescreve o método POST
    def do_POST(self):
        content_length = int(self.headers['Content-length'])
        body = self.rfile.read(content_length).decode('utf-8')
        form_data = parse_qs(body)

        if self.path == '/send_login':
            login = form_data.get('email', [""])[0]
            password = form_data.get('senha', [""])[0]
            logou = self.accont_user(login, password)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(logou.encode("utf-8"))

        elif self.path == '/send_cadastro':
            print("Nome do filme: ", form_data.get('nome_filme', [""])[0])
            print("Nome dos atores: ", form_data.get('nome_atores', [""])[0])
            print("Nome do diretor: ", form_data.get('nome_diretor', [""])[0])
            print("Data: ", form_data.get('ano', [""])[0])
            print("Gênero: ", form_data.get('genero_filme', [""])[0])
            print("Produtora: ", form_data.get('nome_produtora', [""])[0])
            print("Sinopse: ", form_data.get('sinopse', [""])[0])

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Cadastro de filme recebido com sucesso!".encode("utf-8"))

        else:
            super(MyHandle, self).do_POST()


# a main roda o servidor
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server running in http://localhost:8000")
    httpd.serve_forever()

main()
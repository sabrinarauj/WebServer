# importando as bibliotecas do http
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# cria uma classe MyHandle que herda de SimpleHTTPRequestHandler
class MyHandle(SimpleHTTPRequestHandler):

    def list_directory(self, path):
        try:
            # acessa o arquivo index.html e manda uma resposta HTTP ao cliente
            f = open(os.path.join(path, 'index.html'),encoding='utf-8')
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
    
    def accont_user(self, login, password):
        loga = "sabrina@gmail.com"
        senha = "123456"

        if login == loga and senha == password:
            return "Usuário logado"
        else:
            return "Usuário não existe"
    
    # sobrescreve o método GET e verifica se o caminho requisitado é /login
    def do_GET(self):
        if self.path == "/login":
            try:
                # tenta abrir o arquivo login.html no diretório atual do servidor
                with open(os.path.join(os.getcwd(), 'login.html'), encoding='utf-8') as login:
                    content = login.read()
                # manda uma resposta HTTP
                self.send_response(200)
                # cabeçalho da resposta com o tipo de contéudo (html)
                self.send_header("Content-type: ", "text/html")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif (self.path == "/cadastro"):
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

        elif (self.path == "/filmes"):
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

    def do_POST(self):
        if self.path == '/send_login':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            print("Data Form: ")
            print("email: ",form_data.get('email', [""])[0])
            print("password: ",form_data.get('senha', [""])[0])

            login = form_data.get('email', [""])[0]
            password = form_data.get('senha', [""])[0]

            logou = self.accont_user(login, password)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(logou.encode("utf-8"))
        else:
            super(MyHandle, self).do_POST()

    # cadastro
    def do_POST(self):
        if self.path == '/send_cadastro':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            print("Nome do filme: ",form_data.get('nome_filme', [""][0]))
            print("Nome dos atores: ", form_data.get('nome_atores', [""][0]))
            print("Nome do diretor: ",form_data.get('nome_diretor', [""], [0]))
            print("Data: ", form_data.get('ano', [""][0]))
            print("Gênero: ", form_data.get('genero_filme', [""][0]))
            print("Produtora: ", form_data.get('nome_produtora', [""][0]))
            print("Sinopse: ", form_data.get('sinopse', [""][0]))

# a main roda o servidor e chama a classe MyHandle
# cria um caminho localhost e define a porta que irá rodar o servidor
def main():
    server_address = ('',8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server running in http://localhost:8000")
    httpd.serve_forever()
main()
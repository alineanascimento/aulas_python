from flask import Flask


app = Flask(__name__)

@app.route("/") # rota padrao, localhost:5000/ inicial
# o que sera executado 
def hello():
    return "Hello, World!"
@app.route("/sobre") # localhost:5000/sobre
def sobre():
    return "Pagina Sobre"

if __name__ == "__main__":
    app.run(debug=True) # debug=True reinicia o servidor automaticamente quando salvamos o arquivo


# resposta 200 significa que deu tudo certo
# resposta 404 significa que a pagina nao foi encontrada
# resposta 500 significa que deu erro no servidor
# API - Application Programming Interface
"""Interface é uma porta de entrada para um sistema, onde outras 
aplicações podem se conectar e interagir com ele.
Exemplo: API do Twitter, API do Google Maps, API do Facebook, etc."""
"""API REST - representational state transfer
é uma interface que segue os princípios do REST.
protocolo HTTP - Hypertext Transfer Protocol
é o protocolo usado para comunicação entre cliente e servidor na web.
Exemplo: GET, POST, PUT, DELETE, PATCH etc.
"""
# REST - Representational State Transfer
# REST é um conjunto de princípios e restrições para a construção de APIs web.
# RESTful é uma API que segue os princípios do REST.

"""Cliente -> 
Requisição (GET, POST, PUT, DELETE) -> 
Servidor -> Resposta (200, 404, 500) -> Cliente"""
"""cliente -> request -> API -> API server -> response -> API -> cliente"""

# clinete -> servidor 
# -> HTTP : get, post, put, delete, patch
#URL /hello_world
# -> Resposta : 200, 404, 500
# -> Dados : JSON, XML, HTML, TEXT
#formas de devolver pro cliente json, xml, html, text


#API REST X API RESTful
"""
- API REST é uma API que segue os princípios do REST. estilo de arquitetura
- API RESTful é uma API que segue os princípios do REST e é fácil de usar e entender
- get é usado para retornar dados
- post é usado para inserir informações em um recurso específico
- put é usado para atualizar um recurso específico, substitui todas as informações do recurso
- patch é usado para atualizar um recurso específico, substitui apenas as informações que foram enviadas ou seja parciais
- delete é usado para deletar um recurso específico
- recurso é uma entidade que pode ser acessada via API, por exemplo: usuário, produto, pedido, etc.
- endpoint é a URL onde o recurso pode ser acessado, por exemplo: /users, /products, /orders, etc.
- verbo HTTP é a ação que será executada no recurso, por exemplo: GET, POST, PUT, DELETE, PATCH
"""
"""Codigos de status de resposta HTTP
100-199: Informational (nao diz se deu certo ou nao)
200-299: Success
300-399: Redirection (redirecionamento), acontece quando a URL mudou de lugar
400-499: Client Error (erro do cliente) errou o formato por exemplo, o cliente que errou
500-599: Server Error (erro do servidor) deu erro no servidor, cliente fez tudo certo mas
o servidor que deu erro, nao conseguiu processar a requisicao
Exemplos:
200 OK: A requisição foi bem-sucedida.
201 Created: A requisição foi bem-sucedida e um novo recurso foi criado.
204 No Content: A requisição foi bem-sucedida, mas não há conteúdo para retornar.
400 Bad Request: A requisição não pôde ser entendida pelo servidor devido a sintaxe incorreta.
401 Unauthorized: A requisição requer autenticação do usuário.
403 Forbidden: O servidor entendeu a requisição, mas se recusa a autorizá-la.
404 Not Found: O servidor não encontrou o recurso solicitado.
500 Internal Server Error: O servidor encontrou uma condição inesperada que o impediu de atenderr a requisição.
502 Bad Gateway: O servidor, ao atuar como gateway ou proxy, recebeu uma resposta inválida do servidor upstream.
503 Service Unavailable: O servidor não está pronto para manipular a requisição. Causas comuns são o servidor estar sobrecarregado ou em manutenção.
"""


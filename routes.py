from flask import Flask, request

from main import insertUser

app = Flask("Raul-Python-Flask")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return{"Ola":"Mundo"}

@app.route("/cadastrar/usuario", methods=["POST"])
def cadastraUsuario():
    
    body = request.get_json()

    if("nome" not in body):
        return geraResponse(400, "O parâmetro nome é obrigatorio")
    if("email" not in body):
        return geraResponse(400, "O parâmetro email é obrigatorio")
    if("idade" not in body):
        return geraResponse(400, "O parâmetro idade é obrigatorio")

    usuario = insertUser(body["nome"], body["email"], body["idade"])

    return geraResponse(200, "Usuário criado com sucesso!", "user", usuario)

def geraResponse(status, mensagem, nome_conteudo = False, conteudo = False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_conteudo and conteudo):
        response[nome_conteudo] = conteudo
    
    return response

app.run()
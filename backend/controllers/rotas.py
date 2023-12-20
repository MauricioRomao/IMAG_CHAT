from backend import *
from flask import Flask, render_template,redirect,request,flash,session,abort,url_for,jsonify, request
import json
import requests as requests




#
# @app.route('/home')
# @app.route('/')
# def home():
#     return render_template('index.html')
# @app.route("/criar/<nome>/<email>", methods=['GET', 'POST'])
# def criar(nome,email):
#     dados = {
#         'nome': nome,
#         'email': email
#     }
#     requisicao = requests.post(f"{config['databaseURL']}/.json", data=json.dumps(dados))
#     print(requisicao)
#     print(requisicao.text)
#     return "pagina de criar login"


# @app.route("/chat", methods=['GET','POST'])
# def chat():
#     return jsonify({
#         "mensagem":"ola do python"
#     })
id_user=None
@app.route("/criar", methods=['GET','POST'])
def criar():
    nome=request.json('nome')
    email=request.json('email')
    senha=request.json('senha')
    dados={
        'NOME COMPLETO':nome,
        'EMAIL PRINCIPAL':email,
        'SENHA':senha

    }
    requisicao=request.post(f"{config['databaseURL']}/.json", data=json.dumps(dados))
    dic=requisicao.json()
    for id in dic:
        print(id)
        id_user=id




    return jsonify({
         "identificação":id_user
    })



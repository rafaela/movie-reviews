#coding: utf-8

import json
from ModuloTwitter import twitter as tt
from ModuloTMD import tmd as tm

from flask import Flask, render_template, request

app = Flask(__name__)

''' Rota para renderizar a página inicial da aplicação'''
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", status=201)


'''Busca por tweets que possuam determinado termo usando módulo'''
def search_tweets(termo):
    tweety = tt.Tweety()
    result = tweety.search_term(termo)
    return tweety.filter(result)

def search_film(filme):
    filmeApi = tm.TmdAPI()
    return filmeApi.filme(filmeApi.request_filme(filme))

@app.route('/comentarios', methods=['GET'])
def search():
    query = request.args.get('name')

    if query == "":
        return render_template("index.html", status=404)

    jsonResponse = json.loads(search_film(query))

    if jsonResponse['status'] == 404:
        return render_template("index.html", status=404)

    twetts = search_tweets("'"+query+"'")

    return render_template("index.html", filme=jsonResponse, query=query, t = twetts, status=200)

'''__main__'''
if __name__ == "__main__":
    app.run(debug=True, port=8080)

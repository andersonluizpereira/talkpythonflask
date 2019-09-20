import requests
from datetime import datetime
from flask import Flask, abort, jsonify, request
import hashlib

config = {
         "limit":'10',
         "version":"/v2/",
         "urlbase":"http://pokeapi.co/api",
         "urlmiddle":"pokemon/"
         }

headers = {
    'Accept': "*/*",
    'Accept': "application/json,*/*",
    'Cache-Control': "no-cache",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/api/v1.0/pokemon/<nome>", methods=['GET'])
def pokemonnome(nome='ditto'):
    url=''+config.get('urlbase')+config.get('version')+config.get('urlmiddle')+str(nome)+'/'
    print(url)
    res = requests.get(url)
    return  jsonify(res.json()), 200


@app.route("/api/v1.0/pokemon/", methods=['GET'])
@app.route("/api/v1.0/pokemon/<int:numero>", methods=['GET'])
def pokemonid(numero=1):
    url=''+config.get('urlbase')+config.get('version')+config.get('urlmiddle')+str(numero)
    print(url)
    res = requests.get(url)
    return  jsonify(res.json()), 200

@app.route("/api/v2.0/pokemon/", methods=['GET'])
@app.route("/api/v2.0/pokemon/<int:numero>", methods=['GET'])
def pokemon(numero=1):
    url=''+config.get('urlbase')+config.get('version')+config.get('urlmiddle')+str(numero)
    print(url)
    res = requests.get(url,headers)
    return  jsonify(res.json()), 200



if __name__ == '__main__':
    app.run(debug=True)
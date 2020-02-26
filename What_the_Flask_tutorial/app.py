from flask import Flask, jsonify


app = Flask('What_the_Flask_Tutorial')

def json_api():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]

    return jsonify(pessoas=pessoas, total=len(pessoas))

app.run()
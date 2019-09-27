from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/pokemon/<string:pokemon_name>')
def get_pokemon_by_name(pokemon_name):
    response = requests.get('https://pokeapi.co/api/v2/pokemon-species/%s' % pokemon_name)
    return jsonify(response.json())


app.run(port=5000)
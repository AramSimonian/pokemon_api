import requests
import json
import sys

def get_pokemon_response(pokemon_name):
    try:
        response = requests.get('https://pokeapi.cox/api/v2/pokemon-species/%s' % pokemon_name)
        return response.json()
    except:
        return "Error calling Pokemon API: " + str(sys.exc_info()[0])
    

print(get_pokemon_response("charizard"))
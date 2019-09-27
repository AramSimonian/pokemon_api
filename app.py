from flask import Flask, jsonify
import requests
import json

language_code = "en"

app = Flask(__name__)

def extract_ft_for_language(flavor_text_entries, language_code):
    ft_for_language = []
    for fte in flavor_text_entries:
        # The language code is stored within a sub-dictionary
        if fte["language"]["name"] == language_code:
            # \n will break the API call
            ft_for_language.append(fte["flavor_text"].replace('\n', ' '))

    # This will contain a list of descriptions for a character
    # from all the different game versions
    return ft_for_language


@app.route('/pokemon/<string:pokemon_name>')
def get_pokemon_by_name(pokemon_name):
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon-species/%s' % pokemon_name)

        fte_all = response.json()["flavor_text_entries"]
        ft_for_language_all = extract_ft_for_language(fte_all, language_code)

        # Just choose the first description
        # until requirements change
        pokemon_description = ft_for_language_all[0]

        

        return jsonify(pokemon_description)
    except:
        return 'Sorry, that Pokemon name was not found'

app.run(port=5000)
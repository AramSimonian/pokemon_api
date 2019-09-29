from flask import Flask, jsonify
import requests
import json

language_code = "en"

app = Flask(__name__)

def clean_string(source_string):
    output = source_string.replace('\n', '')
    output = output.replace('  ', ' ')
    return output

def extract_ft_for_language(pokemon_response, language_code):
    fte_all = pokemon_response["flavor_text_entries"]
    ft_for_language = []
    for fte in fte_all:
        # The language code is stored within a sub-dictionary
        if fte["language"]["name"] == language_code:
            # line breaks will break the API call
            ft_for_language.append(clean_string(fte["flavor_text"]))

    # This will contain a list of descriptions for a character
    # from all the different game versions
    return ft_for_language

def extract_translation(shakespeare_response):
    return shakespeare_response.json()["contents"]["translated"]

def get_pokemon_response(pokemon_name):
    return requests.get('https://pokeapi.co/api/v2/pokemon-species/%s' % pokemon_name)

def get_shakespearean_response(modern_english):
    querystring = {'text':modern_english}
    return requests.request("GET",'https://api.funtranslations.com/translate/shakespeare.json', params=querystring)

@app.route('/pokemon/<string:pokemon_name>')
def get_pokemon_translation(pokemon_name):
    try:
        pokemon_response = get_pokemon_response(pokemon_name)

        ft_for_language_all = extract_ft_for_language(pokemon_response.json(), language_code)

        # Just choose the first description until requirements change
        pokemon_description = ft_for_language_all[0]

        try:
            # Translate the description to Shakespearean English
            shakespeare_response = get_shakespearean_response(pokemon_description)
            description_output = extract_translation(shakespeare_response)
        except:
            description_output = "Error calling Shakespeare API (site lists a limit of five calls per hour)"
        finally:
            output = {
                "name" : pokemon_name,
                "description" : description_output
            }

        return output
    except:
        return 'Error calling Pokemon API'

app.run(port=5000)
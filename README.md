# pokemon_api
REST API that accepts a Pokémon character name and returns its description, translated into Shakespearean English

## Installation
Start by installing Python for your OS:
```
https://www.python.org/downloads/
```

You'll also need a couple of libraries to run this code.  My preferred installer is pip:
```
pip3 install flask
pip3 install requests
```

If you have an issue with permissions when installing, then add `--user` to add the library just to your profile.

To test the API from the command line install this as well:
```
pip3 install httpie
```

## Usage
To execute the code, naviagate to the folder and run:
```
python3 app.py
```

Think of a Pokémon character name (e.g. `charizard`) and, if using a browser, navigate to:
```
http://localhost:5000/pokemon/charizard
```

If you've installed `httpie` (see above) then run this:
```
http http://localhost:5000/pokemon/charizard
```

## Ouput
The output will be of the form:
```
{
  "name": "charizard",
  "description": "Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However, 't nev'r turns its fiery breath on any opponent weaker than itself."
}
```
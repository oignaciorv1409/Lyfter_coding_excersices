import json

# Json dict a texto
b = {
        "name": "Bulbasaur",
        "type": [
                "Grass",
                "Poison"
        ],
        "stats": {
                "hp": 45,
                "attack": 49,
                "defense": 49
        }
}

#parse with dumps()
load_pokemon = json.dumps(b)

print(load_pokemon)
print(type(load_pokemon))





# convertir txt JSON a Dict 

import json

pokemon_json = '{"name": "Bulbasaur","type": ["Grass", "Poison"]}'


#parse with loads()

pokemon_dict = json.loads(pokemon_json)

print(pokemon_json)
print(pokemon_dict["name"])
print(type(pokemon_dict))


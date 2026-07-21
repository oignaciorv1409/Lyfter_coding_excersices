import json

new_data = {
        "name": "Charizard",
        "type": "Fire/Flying",
        "level": 58,
        "weight_kg": 90.5,
        "is_shiny": False,
        "held_item": None,
        "skills": [
        "Flamethrower",
        "Air Slash",
        "Dragon Claw",
        "Fire Spin"
        ],
        "stats": {
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "sp_attack": 109,
        "sp_defense": 85,
        "speed": 100
        }
}


with open("pokemon_file.json", "r", encoding='utf-8') as file:
        existing_data = json.load(file)

existing_data.append(new_data)

with open("pokemon_file.json", "w", encoding='utf-8') as file:
        json.dump(existing_data, file, indent=4)
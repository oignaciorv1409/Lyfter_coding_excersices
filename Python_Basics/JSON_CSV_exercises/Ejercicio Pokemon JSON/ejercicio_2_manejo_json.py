import json


def read_pokemon_file(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
                pokemon_list = json.load(file)

        return pokemon_list


def get_new_pokemon():
        name = input("Pokemon name: ")
        pokemon_type = input("Pokemon type: ")
        level = int(input("Pokemon level: "))
        weight_kg = float(input("Pokemon weight in kg: "))


        new_pokemon = {
                "name": name,
                "type": pokemon_type,
                "level": level,
                "weight_kg": weight_kg
        }

        return new_pokemon


def save_pokemon_file(file_path, pokemon_list):
        with open(file_path, "w", encoding="utf-8") as file:
                json.dump(pokemon_list, file, indent=4)


def main():
        file_path = "pokemon_file.json"

        pokemon_list = read_pokemon_file(file_path)

        new_pokemon = get_new_pokemon()

        pokemon_list.append(new_pokemon)

        save_pokemon_file(file_path, pokemon_list)


main()
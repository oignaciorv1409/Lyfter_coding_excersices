n = int(input("How many games are you adding? "))

def user_input ():
        name = input("Please enter the name: ")
        genre = input("Please enter the genre: ")
        dev = input("Please enter the developer: ")
        rate = input("Please enter ESRB rate: ")

        games_dict = {
                
                "Name": name,
                "Genre": genre,
                "Developer": dev,
                "ESRB": rate
                
                }
        
        return games_dict


def create_list_of_dict (n):
        videogames = []

        for i in range(n):
                game = user_input()
                videogames.append(game)

        return videogames


def save_games_in_file (filepath, data):
        import csv

        with open(filepath, "w", encoding="utf-8", newline= "") as file:

                headers = data[0].keys()

                writer = csv.DictWriter(file, fieldnames= headers)

                writer.writeheader()

                writer.writerows(data)


def main():
        videogames = create_list_of_dict(n)
        save_games_in_file("videogames.csv", videogames)


main()
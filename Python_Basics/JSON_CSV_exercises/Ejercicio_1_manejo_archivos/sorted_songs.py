def read_filter_songs (input_file):
        songs_list = []
        
        with open (input_file, "r", encoding="utf-8") as file:
# Usando readlines() para crear una lista no ordenada
                songs = file.readlines()


        for song in songs:
                song = song.rstrip()

                if song.startswith("*"): # Agrego esto para filtrar el dato, songs.txt, empieza con un comentario -> '* This is my list of some of my liked songs in YT music app. *\n',
                        continue
                elif song == "\n":   # Agrego el salto de linea para que no salga en la lista 
                        continue     # ['\n', 'Asi mismo - Canserbero\n',
                else:
                        songs_list.append(song)
        
        return songs_list


def to_sort_songs (songs_list):
        songs_list.sort()
        return songs_list



def write_songs (output_file, songs_list):
        with open(output_file, "w", encoding= "utf-8") as file:
                for song in songs_list:
                        file.write(song + "\n")

        with open(output_file, "r", encoding="utf-8") as file:
                print(file.read())


def main ():
        songs = read_filter_songs("songs.txt")
        sorted_songs = to_sort_songs(songs)
        output_file = write_songs("sorted_songs.txt", sorted_songs)

main()
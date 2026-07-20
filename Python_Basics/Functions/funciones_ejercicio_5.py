text = "Hello World"

def reversed_iteration (text):
        reversed_text = ""   #"caja vacia"

        for caracter in reversed(text):
                reversed_text += caracter  # Sumar o acumular srings un caracter por vuelta del ciclo for 
        
        return reversed_text

reversed_caracter = reversed_iteration(text)
print(reversed_caracter)

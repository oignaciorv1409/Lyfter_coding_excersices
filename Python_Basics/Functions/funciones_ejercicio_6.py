# "I love Nación Sushi" -> "There's 3 upper cases and 13 lower cases"

text = "I love Nación Sushi"

def get_lower_and_upper_case (text):
        uppercase_counter = 0
        lowercase_counter = 0

        for caracter in text:
                if caracter.isupper():
                        uppercase_counter += 1
                
                elif caracter.islower():  # Si uso else eso cuenta todo lo que no sea upper case, incluyendo espacios, comas y puntos.
                        lowercase_counter += 1

        print (F"There's {uppercase_counter} upper cases and {lowercase_counter} lower cases.")

get_lower_and_upper_case(text)
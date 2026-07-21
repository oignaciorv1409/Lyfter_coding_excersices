while True:
        main_input = input("Ingrese la edad: ")
        try:
                age = int(main_input)
                if age < 0:
                        print("Edad no puede ser negativa o menor a cero. Intenta de nuevo.")
                        
                        continue
                break
        except ValueError:
                print("Porfavor ingrese un numero valido (numeros enteros)")

if 0 <= age <= 1:
        category = "Bebe"
elif 2 <= age <= 11: 
        category = "niño"
elif age == 12:
        category = "preadolescente"
elif 13 <= age <= 17:
        category = "adolescente"
elif 18 <= age <= 29:
        category = "adulto joven"
elif 30 <= age <= 59:
        category = "adulto"
elif 60 <= age <= 120:
        category = "adulto mayor"
else:
        category = None

if category:
        print("La edad se encuentra en la categoria:", category)
else:
        print("No se encontro una categoria para esa edad.")
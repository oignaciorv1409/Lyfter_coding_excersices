# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

# 1. Ejemplos:
# 2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.


# n = int(input("ingrese un numero: ")) --> Necesito pedirlo 10 veces. Debe ir dentro del ciclo For

# highest_number = None  --> TypeError: '>' not supported between instances of 'NoneType' and 'NoneType'
highest_number = 0

ten_numbers = []

for n in range(10):
        n = int(input("ingrese un numero: "))
        # n = highest_number --> Esto sobreescibe el numero del usuario

        ten_numbers.append(n) # Aqui si los guardo en la lista 
        # if highest_number > n: --> esta logica esta mal deberia comparar n contra el primer numero que es
                # highest_number = highest_number
        # else:
                # n = n
                # ten_numbers.append(highest_number)
        if n > highest_number:
                highest_number = n

print(ten_numbers)
print(F"El numero mayor es: {highest_number}")
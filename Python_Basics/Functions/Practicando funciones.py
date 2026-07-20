# Las funciones son un bloque reutilizable de codigo, son como una receta o mini maquina con una funcion especifica
# se crean con def, ejemplo:

#IMPORTANTE: Definir una funcion (def) no es lo mismo que ejecutarla

def greet(name):
        print(f"Hola {name}")

greet("Edgar")  # Aqui estoy llamando la funcion con greet("Edgar") y el parametro (placeholder) que en este caso es <name>, recibe el valor  "Edgar" y "Edgar es un argumento" cuando llamamos a la funcion

# parámetro = variable que la función espera recibir  (name)
# argumento = valor real que le pasas al llamarla (Edgar)
# mutabilidad no define al parámetro; depende del tipo de dato que reciba (String, int, lista, diccionarios...)

# la funcion puede imprimir algo (print) o devolver algo (return)

def sum_numbers(a, b):
        print(a + b)

sum_numbers(3, 4)

# en este ejemplo esta imprimiendo el resultado de la suma entre los argumento 3 y 4, pero no esta devolviendo el resultado para usarlo despues

# Ejemplo con return 

def sum_two_nunbers(a, b):
        return a + b

result = sum_two_nunbers(3, 4)
print(result) 

# En este ejemplo estoy guardando la operacion o suma de esos numeros en una variable llamada "result"
# Ademas devuelve el resultado 7

# Diferencia, print devuelve salida en pantalla pero no un valor util que pueda usar 
# return entrega un valor que podemos usar depues y ese valor se puede guardar, reutilizar o combinar

# analogia, la funcion es una maquina de palomitas 
# con print la maquina me enseña las palomitas "Aqui esta el 7"
# Pero con return, la maquina me entrega el vaso en la mano entonces
#  y puedo guardar las palomitas, usarlas despues o darsela a otra maquina (otra funcion)

# IMPORTANTE -> Cuando python ejecuta un return, la funcion termina 
# devuelve valor y sale de la funcion (similar a break)
# lo que venga despues dentro de esa funcion (mini maquina) no se va a ejecutar

# Una funcion puede tener varios return pero solo se ejecuta el primero que se alcance o sea verdadero

def get_max(a, b):
        if a > b:
                return a
        return b

# En este caso solo devuelve b si la condicion en el primer return fue falsa


# Tambien se pueden asignar a los parametros un valor por defecto u opcionales, ej: 

def print_sum_of_numbers(number_a, number_b=5):
        print(number_a + number_b)

print_sum_of_numbers(4) # Aqui el argumento solo aplica para el "number_a"

# El resultado es 9 porque como no le pase un argumento para el parametro "number_b" el resultado de la suma es 4 + 5 = 9

#IMPORTANTE -> Hay una regla de que los parametros opcionales deben ir depues de los parametros normales (obligatorios)

# def greet(name, greeting="Hola"):  # CORRECTO

# def greet(greeting="Hola", name):  # INCORRECTO


# IMPORTANTE: Las funciones dividen problemas mas grandes en partes pequeñas
# EN programacion es central el principio DRY
# SI la funcion tiene que usar un "and" para hacer mas de una cosa probablemente no es el mejor uso de esa funcion 
# Repetir el codigo es una mala practica porque se vuelve mas largo y dificil de leer
# Mas dificil de corregir y dificil de mdificar 

# Practica: 

# Full name: Ignacio Rodriguez

def get_name(first_name, last_name):
        return first_name, last_name

full_name = get_name("Ignacio", "Rodriguez")
print(f"Mi nombre es {full_name}")


def get_name(first_name, last_name="Rodriguez"):
        return first_name + last_name

full_name = get_name("Ignacio")
print(f"Mi nombre es {full_name}")



# V2
def get_full_name(first_name, last_name):
        return f"{first_name} {last_name}"

full_name = get_full_name("Ignacio", "Rodriguez")
print(f"Mi nombre es {full_name}")


def get_full_name(first_name, last_name="Rodriguez"):
        return first_name + " " + last_name

full_name = get_full_name("Ignacio")
print(f"Mi nombre es {full_name}")



#solo con print

def print_full_name(first_name, last_name):
        print(f"Full name: {first_name} {last_name}")

print_full_name("Ignacio", "Rodriguez")


def sum_two_numbers(number_a, number_b):
        return number_a + number_b

result_of_sum = sum_two_numbers(6, 4)
print(result_of_sum)






def get_square(number):
        return number ** 2

result = get_square(5)
print(result)


user_number = int(input("Ingrese un numero: "))

def is_even(num):
        return num % 2 == 0

module_cal = is_even(user_number)
print(module_cal)
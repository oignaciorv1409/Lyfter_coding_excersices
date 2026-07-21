# [1, 4, 6, 7, 13, 9, 67] -> [7, 13, 67]

# Un numero es primo si es mayor que 1 y es divisible por 1 y por si mismo (o tiene dos divisores).. Si el numero es 1 no es primo, entonces se puede empezar desde el rango 2 hasta num en el ciclo For
# El For debe recorrer los numeros para confirmar que ninguno puede dividir el numero actual solo el numero actual se puede dividir a si mismo (o el 1) 
# No hace falta probar que el numero se div a si mismo solo que otros numeros lo hagan excepto el 1 y eso confirma que no es primo


def is_prime (num):
        if num <= 1:
                return False
        for i in range(2, num):
                if num % i == 0:
                        return False
        else:
                return True 



def get_prime_numbers (list_of_numbers):

        prime_numbers = []

        for num in list_of_numbers:
                if is_prime(num):
                        prime_numbers.append(num)
        
        return prime_numbers

list_of_numbers = [1, 4, 6, 7, 13, 9, 67]
result = get_prime_numbers(list_of_numbers)
print (result)
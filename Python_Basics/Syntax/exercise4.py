# Cree un programa que elimine todos los números impares de una lista.

# 1. Ejemplos:
# 2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`


temp_list = []
#anterior --> temp_list = 0 "Traceback: AttributeError: 'int' object has no attribute 'append'

my_list = [1,2,3,4,5,6,7,8,9,10]

for n in my_list:
        if n % 2 == 0:
                temp_list.append(n)
                #print(temp_list, my_list) --> Afuera del cliclo For para que no imprima cada iteracion

print(temp_list, my_list)
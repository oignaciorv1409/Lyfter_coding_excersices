my_dream_car = "Porche Cayenne GTS"
#for i in range(len(my_dream_car)):
#       print([i, my_dream_car])

#[0, 'Porche Cayenne GTS']
#[17, 'Porche Cayenne GTS'] 
# range(0, 17)
# EL step debe ser de 1 en 1 pero haca atras, es decir: 17,0,-1

#for i in range(len(my_dream_car)) -1:
#        print(my_dream_car[i])

for i in range(len(my_dream_car)):
        print(i, my_dream_car[i])

# De esta manera no imprime todo el string 17 veces y solo imprime el indice de cada caracter en el string my_dream_car

for i in range(len(my_dream_car)-1, -1, -1):
        print(my_dream_car[i])

# Aqui le estoy diciendo a Python que vaya del indice 17 al 0 (start = 17, stop = 0, step -1)
# El step va hacia atras con el -1 y el indice es 17 porque my_dream_car = 18 caracteres. 18 - 1 = 17
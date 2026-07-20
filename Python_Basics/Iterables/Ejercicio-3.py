supermarket_list = ["Eggs", "Chicken", "Onion", "Tomatoes", "Greek Yogurt", "Cheese", "Milk" ]

first_product = supermarket_list[0]  #first_product = "Eggs"

supermarket_list[0] = supermarket_list[-1]  # Eggs [0] pasa a la ultima posicion de la lista [-1] = 6

## first_product = supermarket_list[6] ---> Esta linea esta mal porque estoy sobreescribiendo la posicion de first_product y poniendole el valor de [-1
# Para que funcione necesita ser el ultimo [-1] debe ser igual a la variable temporal first_product

supermarket_list[-1] = first_product

for i in range(len(supermarket_list)):
        print(i, supermarket_list[i])
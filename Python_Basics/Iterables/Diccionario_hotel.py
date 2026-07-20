hotel = {
        "nombre": "Hotel Termales",
        "Estrellas": 3,
        "Habitaciones": [
                {
                        "numero": 1,
                        "precio_por_noche": 50,   # --> Por lo que ve es buena practica escribir los diccionarios de esta forma
                        "piso": 1
                },
                {
                        "numero": 2,
                        "precio_por_noche": 50,
                        "piso": 1
                },
                {
                        "numero": 3,
                        "precio_por_noche": 50,
                        "piso": 1
                },
                {
                        "numero": 4,
                        "precio_por_noche": 50,
                        "piso": 1
                },
                {
                        "numero": 5,
                        "precio_por_noche": 65,
                        "piso": 2
                },
                {
                        "numero": 6,
                        "precio_por_noche": 65,
                        "piso": 2
                },
                {
                        "numero": 7,
                        "precio_por_noche": 65,
                        "piso": 2
                },
                {
                        "numero": 8,
                        "precio_por_noche": 65,
                        "piso": 2
                },
                {
                        "numero": 9,
                        "precio_por_noche": 85,
                        "piso": 3
                },
                {
                        "numero": 10,
                        "precio_por_noche": 85,
                        "piso": 3
                }
        ]
}

print(hotel["nombre"])

print(hotel["Estrellas"])

print(hotel["Habitaciones"]) # --> Un solo diccionario grande repite claves y solo sobrevive la ultima, se necesita un diccionario por habitacion para que la salida refleje cada habitacion

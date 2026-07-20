list_of_keys = ["Login", "Access", "Salary"]

employee = {
        "name": "Ignacio",
        "Last name": "Rodriguez",
        "Age": 29,
        "email": "vosc@amzon.com",
        "Login": "vosc",
        "Level": "L4",
        "Access": 4,
        "Tenure": 2,
}

for key in list_of_keys:
        deleted_keys = employee.pop(key, None)
        # employee.pop(key)
        # employee.pop(key, None) # --> Si agrego None me devuelve None para los keys que no existan
        # employee.pop([Salary], None) # Aqui agrego una clave que no esya en la lista y que no existe en el Diccionario
        # Para poder ver los valores elimnados se tienen que guardad en una variable
        print(key, "->", deleted_keys) #Agrego un print para la variable deleted_keys que guarda los valores eliminados

# deleted_keys = employee.pop(key, None) --> Fuera del ciclo solo imprime el key que no existe en el diccionario "Salary", no imprime los keys que estan dentro del diccionario
print(employee)

global_variable = "This is a global variable."

def get_global_scope ():
        print(global_variable)
        global_variable = "Attempting to modify global variable from local scope."

get_global_scope()  # Python interpreta que la variable que tiene que ejecutar es la variable local pero no tiene valor local o intenta asignarlo antes de imprimir un valor local cuando la lee y por eso da error # "UnboundLocalError: cannot access local variable 'global_variable' where it is not associated with a value" 




def get_variable_locally ():
        local_variable = "This is a local variable."
        print(local_variable)

get_variable_locally()
print(local_variable) # La variable creada localente solo existe dentro de la funcion






# <aside>
# 💪🏽 **Ejercicios**

# Para estos ejercicios debe utilizar solo lo visto en clase. No es valido utilizar funciones como `zip` o `reversed`.**

# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

# 1. Ejemplos:
# 2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
# `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
# Hay casos
# en los
# que la
# iteracion por
# indice es
# muy util
# </aside>


study_tip1 = ["Estudiar", "viente miutos", "y", "por", "permite", "un mayor", "de concentracion.", " se le conoce,", "la tecnica"]

study_tip2 = ["por", "seguidos", "detenerse", "trienta minutos", "desarrollar", "nivel", "A esto,", " como", "POMODORO"]

# Listas de un mismo tamaño y len() solo puede tomar 1 argumento. Usamos 1 lista ya que son del miso tamaño de elementos.
# Anterior: for i in range(len(study_tip1, study_tip2)):
#                   ~~~^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: len() takes exactly one argument (2 given) 

for i in range(len(study_tip1)):
        print(study_tip1[i], study_tip2[i])
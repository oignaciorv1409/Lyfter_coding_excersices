profile_dict = {}

info_list = ["Full name:", "Age:", "Current job:", "Desire Role:"]

my_info_list = ["Ignacio Rodriguez", "29", "Ai annotator", "Software Developer" ]

#for i in range(len(info_list[3])): --> no esta recorriendo toda la lista solo el ultimo elemento 
        #profile_dict = info_list.append(my_info_list)  --> esto solo agrega la lista my_info al final de la lista info

for i in range(len(info_list)):
        profile_dict[info_list[i]] = my_info_list[i] # --> esto en teoria recorre por el indice la lista info y pone en pares usando el indice los valores de la lista

print(profile_dict)
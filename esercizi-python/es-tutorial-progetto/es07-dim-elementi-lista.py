def conta_car(lista_input):
    lista_num = []
    for parola in lista_input:
        lista_num.append(len(parola))
    return lista_num

lista_b = conta_car(['a','bb', 'ccc', 'dddd', 'eeeee'])
print(lista_b)



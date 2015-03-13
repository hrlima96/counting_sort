def count_sort(lista):
    maior = max(lista)
   
    aux = [0 for x in range(maior + 1)]
   
    for num in lista:
        aux[num] += 1
   
    lista = [i for i in range(len(aux)) for j in range(aux[i])]
   
    return lista

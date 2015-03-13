def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]
    
    maior, menor, igual = [], [], []
    
    for num in lista:
        if num > pivo:
            maior.append(num)
        elif num < pivo:
            menor.append(num)
        else:
            igual.append(num)
            
    return quick_sort(menor) + igual + quick_sort(maior)

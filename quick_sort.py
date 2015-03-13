def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]
    
    maior, menor = [], []
    
    for num in lista:
        if num >= pivo:
            maior.append(num)
        else:
            menor.append(num)
            
    return quick_sort(menor) + quick_sort(maior)

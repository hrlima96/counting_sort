def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]
    
    menor = [num for num in lista if num < pivo]
    igual = [num for num in lista if num == pivo]
    maior = [num for num in lista if num > pivo]
            
    return quick_sort(menor) + igual + quick_sort(maior)

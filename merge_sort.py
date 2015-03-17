def merge(lista_1,lista_2):
	if lista_1 == []:
    	return lista_2
  	elif lista_2 == []:
       	return lista_1
	else:
      	if lista_1[0] < lista_2[0]:
          	return [lista_1[0]] + merge(lista_1[1:],lista_2)
      	else:
          	return [lista_2[0]] + merge(lista_1,lista_2[1:])
 
def mergesort(lista):
  	if len(lista) <= 1:
     	return lista
  	else:
    	meio = len(lista) // 2
      	return merge(mergesort(lista[:meio]), mergesort(lista[meio:]))

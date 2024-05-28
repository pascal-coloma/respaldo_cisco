# En este fragmento, se copia parte de la lista
# [x:y] siendo x el indice desde el que comienza la copia
# siendo y, el indice - 1 de la copia
'''miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:6]
print(nuevaLista)'''

# Copiando una lista entera
# Los dos puntos,indica que se copiara todo el contenido de la lista de origen
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)
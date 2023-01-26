lista1 = [1,-1,55,-8]
lista2 = [10,-10,550,-80]
lista3 = [15,-155,555,-85]
lista4 = [lista1,lista2,lista3]
minimumok =[]
def minKeres(lista):
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    print(minimum)
    return minimum

for i in lista4:
    minimumok.append(minKeres(i))
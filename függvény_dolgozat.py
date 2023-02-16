def rendezes(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[j] < lista[i]:
                lista[i],lista[j] = lista[j], lista[i]
    return lista

def minimum_ertek(lista):
    minimum = lista[0]
    for i in lista:
        if i  < minimum:
            minimum = i

    return minimum


def maximum_ertek(lista):
    maximum = lista[0]
    for i in lista:
        if i > maximum:
            maximum = i

    return maximum


lista = [1,9,-6,11,7,12,120,-96,55,42,300,15,-1]
lista = rendezes(lista)
print(lista)
print(minimum_ertek(lista))
print(maximum_ertek(lista))
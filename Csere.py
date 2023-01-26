lista = [9,4,7,10,3,-2,66,-5]


for i in range(len(lista)-1):
    for j in range(i+1 ,len(lista)):
        print(lista)
        if lista[i] > lista[j]:
            lista[i] ,lista[j] = lista[j] ,lista[i]
            print("csere")
        else:
            print('')

print(lista)
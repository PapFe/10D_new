lista = [9,4,7,10,3,-2,66,-5]

for i in range(len(lista),0,-1):
    for j in range(0,i-1):
        if lista[j] > lista[j+1]:
            b = lista[j+1]
            lista[j+1] = lista[j]
            lista[j] = b

print(lista)
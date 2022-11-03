
lista = [1,2,3,4,5,6,7]
lista[0] = 100
print(lista[0])

for i, j in enumerate(lista):
    print(i,j)
    lista[i] = lista[i]+100
    print(i, lista[i])

#lista.append(amit a listába akarsz adni)
#program ami bekér 5 számot,
# ezt eltárolja egy tömbben
#és a végén kiírja a tömböt, az átlágot
#és a legnagyobb értéke, az indexel együtt
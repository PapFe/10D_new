def minimum_ertek(lista):
    min = lista[0]

    for i in lista:
        if i < min:
            min = i

    return min



szamok = []
while True:
    a = int(input("Add meg a számot: "))
    if a != 0:
        szamok.append(a)
    else:
        break

minimum = minimum_ertek(szamok)
print(minimum)
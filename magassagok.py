lista_magassag = []

osztaly_letszam = 3
magassag = 0
for i in range(osztaly_letszam):
    magassag = float(input())
    lista_magassag.append(magassag)

legnagyobb = 0

for i in lista_magassag:
    if i > legnagyobb:
        legnagyobb = i

print(legnagyobb)
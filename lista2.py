#lista.append(amit a listába akarsz adni)
#program ami bekér 5 számot,
# ezt eltárolja egy tömbben
#és a végén kiírja a tömböt, az átlágot
#és a legnagyobb értéke, az indexel együtt

lista = []
osszeg = 0
mximum = -1
for i in range(5):
    a = int(input())
    lista.append(a)
    osszeg = osszeg+a
    if mximum < a:
        mximum = a

print(lista)
print(osszeg/len(lista))
print(mximum,lista.index(mximum))

#lista minden eleméhez hozzáadjuk a maximum
# értéket és elosztjuk átlagga


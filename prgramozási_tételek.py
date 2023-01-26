lista1 = [-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

#lista elemszám.

darab = len(lista1)

print("1. : ",darab)

#van-e negatív szám

i = 0

while i<darab and lista1[i] >= 0:
    i = i+1
if i<darab:
    print("2. : VAN")
else:
    print("2. : Nincs")

#hány páros szám van
count = 0

for i in lista1:
    if i % 2 == 0:
        count = count+1
print("3. : ",count)

#4 maximum érték

maxErtek = lista1[0]

for i in lista1:
    if i > maxErtek:
        maxErtek = i

print("4. : ",maxErtek)

#5. 10-zel osztható

print("5.feladat")
for i in lista1:
    if i % 10 == 0:
        print(i)

#6. első 29-el osztható szám indexe

i = 0
while i < darab and lista1[i] % 29 != 0:
    i = i+1

print("6. : ", i, "érték:", lista1[i])

#7. minden páros-e

Logikai = True

i = 0

while i < darab and lista1[i] % 2 == 0:
    i = i+1

if i < darab:
    Logikai = False

print("7. : ",Logikai)

#8. átlag

atl = 0
osszeg = 0

for i in lista1:
    osszeg = osszeg+i

atl = round(osszeg/darab,2)

print("8. : ",atl)



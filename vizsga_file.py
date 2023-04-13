a = []
with open("autok.csv","r",encoding="UTF8") as file:
    for sor in file:
        a.append(sor.strip().split(";"))

print(a)

a = a[1:]
for i in range(len(a)):
    a[i][4] = int(a[i][4])

indulas = "Munkács"
cel = "Záhony"
ferohely = 0
db = 0
budapest = []

for i in a:
    if i[0] == indulas and i[1] == cel:
            ferohely = ferohely+i[4]

    db = db+i[4]

    if i[0] == "Budapest":
        budapest.append(i[1]+" "+i[3])


atl = round(db/len(a),1)

print("b",ferohely,"\n")
print("c",atl,"\n")
print("d",budapest)

with open("budapest.dat","w",encoding="UTF8") as file:
    for i in budapest:
        file.write(i+"\n")
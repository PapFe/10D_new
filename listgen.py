def rendezes(lista):
    for i in range(0,len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i] < lista[j]:
                lista[i],lista[j] = lista[j],lista[i]


a = []
with open("egysoros.txt","r") as file:
    for sor in file:
        a = sor.strip().split(";")

for i in range(len(a)):
    a[i] = int(a[i])

rendezes(a)
print("EGYSOROS")
print(a)



b = []
with open("többsoros.txt","r") as file:
    for sor in file:
        b.append(sor.strip().split(";"))


for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = int(b[i][j])

print("Többsoros")
for i in range(len(b)):
    rendezes(b[i])
    print(b[i])

egy = ""
for i in a:
    egy = egy+str(i)+";"

with open("egysoros_eredmeny.txt","w") as file:
    file.write(egy)

with open("többsoros_eredmeny.txt","w") as file:
    for i in b:
        sor = ""
        for j in i:
            sor = sor+str(j)+";"

        file.write(sor+"\n")





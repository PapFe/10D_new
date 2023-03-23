def rendezes(lista):
    for i in range(0,len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i] > lista[j]:
                lista[i],lista[j] = lista[j],lista[i]


felsorolas = []
with open("lista.txt","r", encoding="utf-8") as file:
    for sor in file:
        #print(sor)
        felsorolas = sor.strip().split(" ")

for i in range(len(felsorolas)):
    print(felsorolas[i])
    felsorolas[i] = int(felsorolas[i])

rendezes(felsorolas)
st = ""
for i in felsorolas:
    st = st+str(i)+" "
with open("rendezett.txt","w",encoding="utf-8") as file:
    file.write(st+"\n")
    file.write("Minimum: "+str(felsorolas[0])+"\n")
    file.write("Maximum: " + str(felsorolas[len(felsorolas)-1]))

sorok = []
felsorolas = []
with open("himnusz.txt", encoding="utf-8") as file:
    for sor in file:
        print(sor)
        sorok.append(sor.strip())

print(sorok)

with open("felsorolas.txt", encoding="utf-8") as file:
    for sor in file:
        print(sor)
        felsorolas = sor.split(";")

print(felsorolas)

orszag = []
with open("EU.txt", encoding="utf-8") as file:
    for sor in file:
        print(sor)
        orszag.append(sor.strip().split(" "))

print(orszag)


abc = ["egy","kettő","három"]

with open("saját.txt","w",encoding="utf-8") as celfile:
    for i in abc:
        celfile.write(i+",")
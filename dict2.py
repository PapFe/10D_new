konyvek = []
while True:
    cimek = {}
    szerzo = input()
    if szerzo == "":
        break
    else:
        while True:
            cim = input()
            if cim == "":
                break
            else:
                ev = int(input())
                cimek[cim] = ev
        konyvek.append({"Szerző":szerzo,"Művek":cimek})

print(konyvek)


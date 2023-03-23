konyvek = {}
while True:
    cimek = {}
    szerzo = input("Add meg a szerzőt: ")

    if szerzo == "":
        break
    else:
        while True:
            cim = input("Add meg a mű címét: ")
            if cim == "":
                break
            else:
                kategória = input("Add meg a kategóriát: ")
                kiadás = int(input("Add meg a mű kiadási évét: "))
                leírás = input("Add meg a mű leírását: ")
                cimek[cim] = {"Kiadási év":kiadás,"Műfaj":kategória,"Leírás":leírás}
        konyvek[szerzo] = cimek

for szerző,művek in konyvek.items():
    print("Szerző: ",szerző,)
    for cím,adatok in művek.items():
        print("\t könyv: ",cím,)
        for Adat_kulcs,Adat_érték in adatok.items():
            print("\t\t",Adat_kulcs,Adat_érték)

with open("szerzők.txt","w",encoding="utf-8") as file:
    for szerző, művek in konyvek.items():
        file.write("Szerző: "+szerző+"\n")
        for cím, adatok in művek.items():
            file.write("\t könyv: "+cím+"\n")
            for Adat_kulcs, Adat_érték in adatok.items():
                file.write("\t\t"+Adat_kulcs+": "+str(Adat_érték)+"\n")
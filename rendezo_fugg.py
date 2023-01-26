lista2 = [9,4,7,10,3,-2,66,-5]

def rendez(lista,irany):
    for i in range(len(lista)-1):
        for j in range(i+1 ,len(lista)):
            #print(lista)
            if irany == "Nov":
                if lista[i] > lista[j]:
                    lista[i] ,lista[j] = lista[j] ,lista[i]
                    #print("csere")
            else:
                if lista[i] < lista[j]:
                    lista[i] ,lista[j] = lista[j] ,lista[i]
                    #print("csere")


rendez(lista2,"Nov")
print(lista2)
rendez(lista2,"Csok")
print(lista2)
def harommal_oszthatok(lista):
    db = 0
    for i in lista:
        if i%3==0:
            db = db+1

    return db

def is_negative(szam):
    if szam < 0:
        return True
    else:
        return False



#kutya = [1,2,3,4,5,6,7,8,9,12,16]
#db = harommal_oszthatok(kutya)
#print(db)
egyedi_lista = []
while True:
    megadott_szam = int(input())
    if is_negative(megadott_szam):
        break
    else:
        egyedi_lista.append(megadott_szam)

db = harommal_oszthatok(egyedi_lista)
print(db)

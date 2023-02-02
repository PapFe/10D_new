def harommal_oszthatok(lista):
    db = 0
    for i in lista:
        if i%3==0:
            db = db+1

    return db

kutya = [1,2,3,4,5,6,7,8,9,12,16]

db = harommal_oszthatok(kutya)
print(db)
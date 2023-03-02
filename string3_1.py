szovegem = input()
db = 0
szamok = "0123456789"
for i in szovegem:
    if i in szamok:
        db = db+1
        print(i)

print(db)
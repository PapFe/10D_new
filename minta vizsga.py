print("1. feladat")
a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy számot: "))
if a > b:
    print("Az elő szám a negyobb",a)
elif b > a:
    print("A második szám a negyobb", b)
else:
    print("A két szám egyenlő")


print("2. feladat")

def kodolas(mondat,betu,darab):
    cserel = ""
    db = 0
    for i in mondat:
        if i == betu and db < darab:
            cserel=cserel+str(ord(i))
            db = db+1
        else:
            cserel = cserel + i
    return cserel

szoveg = kodolas("Valami szöveget kell megadni","a",2)
print(szoveg)

a = []
with open("autok.csv","r",encoding="UTF8") as file:
    for sor in file:
        a.append(sor.strip().split(";"))

print(a)
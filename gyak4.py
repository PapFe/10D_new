szam = int(input())

logikai = True

#for i in range(2,szam,1):
 #   if szam % i == 0:
  #      logikai = False


j = 2
while logikai and j < szam:
    if szam % j == 0:
        logikai = False
    else:
        j = j+1

if logikai:
    print("prímszám")
else:
    print("Nem prím szám")
import math

a = int(input())
b = int(input())

muvelet = input()

eredmeny = -1

if muvelet == "+":
    eredmeny = a+b
elif muvelet == "-":
    eredmeny = a-b
elif muvelet == "*":
    eredmeny = a*b
elif muvelet == "/":
    eredmeny = a/b
elif muvelet == "**":
    eredmeny = a**b
elif muvelet == "sqrt":
    eredmeny = math.sqrt(a)
# Hatványozás, gyökvonás,

else:
    print("Nincs ilyen művelet")

print(eredmeny)

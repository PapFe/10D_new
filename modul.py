import math as m


# 5x2 -3x -2 = 0
a = 5
b = -3
c = -2


D = m.pow(b,2)-4*a*c
print(D)

if D > 0:
    print("Két gyök lesz")
    X1 = (-1 * b + m.sqrt(D)) / (2 * a)
    X2 = (-1 * b - m.sqrt(D)) / (2 * a)
    print(X1)
    print(X2)
elif D == 0:
    print("EGy gyök lesz")
    X1 = (-1 * b + m.sqrt(D)) / (2 * a)
    X2 = (-1 * b - m.sqrt(D)) / (2 * a)
    print(X1)
    print(X2)

X1 = (-1 * b + m.sqrt(m.pow(b,2)-4*a*c)) / (2 * a)


else:
    print("Nincs valós gyök")

if(5*m.pow(X1,2)-3*X1-2==0):
    print("Helyes")





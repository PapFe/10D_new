import math

pi=math.pi

for i in range(5):
    print("print kérem válasszon az alábbi opciók közűl: 0: Kör terület, kerület számítás. páros szám: négyzet számítás")
    a = int(input())
    if a == 0:
        print("Kérem adja meg a kör sugarát")
        r = float(input())
        T = round(r**2*pi,2)
        K = round(2*r*pi,2)
        print("A kör opciót választotta. A kör sugara: ",r,". Területe: ",T,". Kerülete: ",K,".")
    elif a % 2 == 0:
        print("A négyzet opciót válaszotta. A ",a," páros szám. A szám négyzete: ",a**2)
    else:
        print("Nincs ilyen opció")
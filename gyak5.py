#  F to C = (F-32)/1.8
# C to F = C*1.8+32
# C to K = C+273.15
# K to C = K-273.15

homerseklet = float(input("Add meg az alap hőfokot: "))
print("Add meg a mérték egységet. C = celsius, F = Fahrenheit, K = Kelvin")
mertekegyseg = input()

if mertekegyseg == "C":
    #Alap hőmérséklet celsius egységben van
    #celsiust nem kell számolni
    #F-et kell számolnom C to F = C*1.8+32
    #Ezt külön változóba teszem
    #kiiratom az összes egység szerint
    F = homerseklet*1.8+32
    K = homerseklet+273.15
    print("A hőmérséklet celsiusban: ",homerseklet)
    print("A hőmérséklet fahrenheit-ben: ",F)
    print("A hőmérséklet Kelvin-ben: ", K)
elif mertekegyseg == "F":
    C = (homerseklet-32)/1.8
    K = C+273.15
    print("A hőmérséklet fahrenheit-ben: ", homerseklet)
    print("A hőmérséklet celsiusban: ", C)
    print("A hőmérséklet Kelvinben: ", K)
elif mertekegyseg == "K":
    C = homerseklet-273.15
    F = C*1.8+32
    print("A hőmérséklet fahrenheit-ben: ", F)
    print("A hőmérséklet celsiusban: ", C)
    print("A hőmérséklet Kelvinben: ", homerseklet)
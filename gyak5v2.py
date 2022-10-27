#  F to C = (F-32)/1.8
# C to F = C*1.8+32
# C to K = C+273.15
# K to C = K-273.15

homerseklet = float(input("Add meg az alap hőfokot: "))
print("Add meg a mérték egységet. C = celsius, F = Fahrenheit, K = Kelvin")
mertekegyseg = input()
mibe = input()



if mertekegyseg == "C":

    if mibe == "C":
        print("A ",homerseklet," Celsius fok az ",homerseklet," Celsius fok")
    elif mibe == "F":
        F = homerseklet*1.8+32
        print("A ", homerseklet, " Celsius fok az ",F, " Fahrenheit")
    elif mibe == "K":
        K = homerseklet + 273.15
        print("A ", homerseklet, " Celsius fok az ",K, " Kelvin")

elif mertekegyseg == "F":
    if mibe == "C":
        C = (homerseklet-32)/1.8
        print("A ", homerseklet, "  Fahrenheit az ", C, " Celsius fok")
    elif mibe == "F":
        print("A ", homerseklet, " Fahrenheit az ", homerseklet, " Fahrenheit")
    elif mibe == "K":
        K = ((homerseklet-32)/1.8) + 273.15
        print("A ", homerseklet, " Fahrenheit fok az ", K, " Kelvin")
elif mertekegyseg == "K":
    if mibe == "C":
        C = homerseklet-273.15
        print("A ", homerseklet, "  Kelvin az ", C, " Celsius fok")
    elif mibe == "F":
        F = (homerseklet-273.15)*1.8+32
        print("A ", homerseklet, " Kelvin az ", F, " Fahrenheit")
    elif mibe == "K":
        print("A ", homerseklet, " Kelvin az ", homerseklet, " Kelvin")
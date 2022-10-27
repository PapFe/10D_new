
jomegoldas = "abcd"
megoldas = "abcd"
a = False
b = False
C = False
d = False
for i in jomegoldas:
    for j in megoldas:
        if j == i:
            if i == "a":
                a = True
            elif i == "b":
                b = True
            elif i == "c":
                c = True
            elif i == "d":
                d = True
if a and b and c and d:
    print("GOOD")
else:
    print("bad")


c = "hfa"
h = ""
for i in range(len(c)-1,-1,-1):
    h = h+c[i]

print(h)


print("A")
a = "sós"
print(a[::-1])
print()
print("B")
if a == a[::-1]:
    print("palindrom")
else:
    print("Nem palindrom")
print()
print("C")
mondat = "Az alma a fán piros"
szó = ""

for i in mondat:
    if i == " ":
        print(szó)
        szó = ""
    else:
        szó = szó+i

print(szó)



for i in mondat.split(" "):
    print(i)
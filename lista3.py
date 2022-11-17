
l = [1,2,3,4,5]
print(l[0])
for i in l:
    print(i)

for i,elem in enumerate(l):
    print(i,elem)

felhaszl = []
a = 0
for i in range(5):
    a = int(input())
    felhaszl.append(a)
    if a < 0:
        print("kicsi")
    else:
        print(a**2)

for i in felhaszl:
    print(i)


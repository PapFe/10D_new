a = "abcde"

for i in a:
    print(i, end=" ")

print()

for j in range(0,len(a),2):
    print(a[j], end=" ")

print()

for k in a:
    print(ord(k), end=" ")
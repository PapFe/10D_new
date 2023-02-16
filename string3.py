print("A")

szó = "hello"
nagy_szó = ""

for i in szó:
    nagy_szó = nagy_szó+chr(ord(i)-32)

print(nagy_szó)

print("B")
nagy_szó = ""
for i in szó[::-1]:
    nagy_szó = nagy_szó+chr(ord(i)-32)

print(nagy_szó)
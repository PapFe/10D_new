himnusz = []
with open("himnusz.txt","r",encoding="utf-8") as file:
    for sor in file:
        himnusz.append(sor.strip())

print(himnusz)
print(len(himnusz))

db = 0
for i in himnusz:
    if i != "":
        db = db+1
print(db)

versszakok = []
versszak = ""
for i in himnusz:
    if i == "":
        versszakok.append(versszak)
        versszak = ""
    else:
        versszak = versszak+i+"\n"

print(versszakok)
for i in versszakok:
    print(i)

print(len(versszakok))

with open("ujhimnusz.txt","w",encoding="utf-8") as ujfile:
    for i in versszakok:
        ujfile.write(i+"\n")

    ujfile.write("Sorok száma: "+str(len(himnusz))+"\n")
    ujfile.write("Sorok száma üres nélkűl: "+str(db)+"\n")
    ujfile.write("Versszakok száma: "+str(len(versszakok))+"\n")
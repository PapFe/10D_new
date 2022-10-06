db = 0
a = 0
avg = 0
for i in range(10):
    a = int(input())
    db = db+1
    avg = avg+a

avg = avg/db
print(avg)
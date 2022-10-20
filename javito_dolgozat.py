a = int(input())
sum = 0
for i in range(5):
    b = int(input())
    sum = sum+b

if sum > a:
    print(sum/5)
else:
    print(sum**2)
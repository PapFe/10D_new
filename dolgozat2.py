
prime = True
i = 2
while prime == True:
    a = int(input())

    if a%2==0:
        print("Hurrá")
    elif a%3 == 0:
        print("hármo a magyar igazság")

    if a <= 10:
        if a == 1:
            print("I")
        elif a == 2:
            print("II")
        elif a == 3:
            print("III")
        elif a == 4:
            print("IV")
        elif a == 5:
            print("V")
        elif a == 6:
            print("VI")
        elif a == 7:
            print("VII")
        elif a == 8:
            print("VIII")
        elif a == 9:
            print("IX")
        elif a == 10:
            print("X")

    if a%2!=0 and a%3!=0 and a >10:
        print("Nem nyert")

    if a != 2:
        prime = False
        while prime == False and i<a:
            if a % i == 0:
                prime = True
            else:
                i = i+1

def rendezo(parameter1,parameter2):
        for i in range(len(parameter1)-1):
            for j in range(i+1, len(parameter1)):
                if parameter2 == 1:
                    if parameter1[i] > parameter1[j]:
                        parameter1[i],parameter1[j] = parameter1[j],parameter1[i]
                elif parameter2 == 0:
                    if parameter1[i] < parameter1[j]:
                        parameter1[i],parameter1[j] = parameter1[j],parameter1[i]
        return parameter1

def max_keres(parameter1):
    maximum_ert = parameter1[0]
    for i in parameter1:
        if i > maximum_ert:
            maximum_ert = i

    return maximum_ert

lista = []
while True:
    szam = int(input())
    if szam == -1:
        break
    else:
        lista.append(szam)


print(lista)
#rendezett = rendezo(lista)
#print(rendezett)
rendezett0 = rendezo(lista,0)
print(rendezett0)
rendezett1 = rendezo(lista,1)
print(rendezett1)

legnagyobb = max_keres(lista)

if legnagyobb % 2 == 0:
    for i in lista:
        if i % 2 == 0:
            print(i)
else:
    for i in lista:
        if i % 2 != 0:
            print(i)


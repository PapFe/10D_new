felsorolas = []

with open("felsorolas.txt", encoding="utf-8") as file:
    for sor in file:
        print(sor)
        felsorolas = sor.split(",")

print(felsorolas)

hossz = len(felsorolas)

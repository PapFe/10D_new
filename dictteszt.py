
car = {
    "model": "base",
    "year":000,
    "color":"base"

}



cars = []
for i in range(2):
    car["model"] = input()
    car["year"] = int(input())
    car["color"] = input()

    cars.append(car)


print(cars)
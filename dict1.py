ember = {
    'név':'Géza',
    'születési_év':1999,
    'lakhely':'Makkoshotyka',
    'foglalkozás':'szarvasmarha-tenyésztő',
    'szemei száma':2,
    'kedvenc lottószámok':[1,2,3,4,5]
}


print(ember)
print(ember.keys())

for i in ember.values():
    print(i)

for i in ember.keys():
    print(i," : ",ember[i])

for i,j in ember.items():
    print(i," : ",j)

print(ember["név"])

ember["kutya"] = "bodri"
print(ember)

ember.pop("szemei száma")
print(ember)

ember["születési_év"] = 1980
print(ember)
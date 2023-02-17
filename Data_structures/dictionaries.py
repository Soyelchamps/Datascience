
# Dictionaries: They are similar like objects in JS, the way the data is stored is with keys and values.
pets = {
    "1": {
        "name": "Moka",
        "age": 3,
        "color": "gray"
    },
    "2": {
        "name": "Capuchino",
        "age": 4,
        "color": "gray"
    },
    "3": {
        "name": "Cereza",
        "age": 5,
        "color": "gray"
    }
}

print(pets)
print(type(pets))
print(len(pets))

for key in pets.keys():
    print("KEY - " + key)

for value in pets.values():
    print("VALUE - ", value)

for k, v in pets.items():
    print("KEY", k, "VALUE", v)

print("FOR IN KEYS")
for key in pets.keys():
    print(pets[key])

print("FOR IN RANGE")
for itr in range(len(pets)):
    print(pets[itr+1])
    print(pets.get(itr+1))


for itr in range(len(pets)):
    print(pets[itr+1])
for itr in range(len(pets)):
    print(pets[itr+1])

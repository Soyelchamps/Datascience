import csv
data = []
rows = []
with open("hurricanes.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)

    for row in reader:
        print(row)
        data.append(row)

print(data)
print("Header -------------", data[0])
print("Content -------------", data[1:])

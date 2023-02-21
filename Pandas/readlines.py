# Open file with open function as readlines
with open("example.csv", "r") as file:
    content_data = file.readlines()

content_header = content_data[0:1]
content_rows = content_data[1:]
print(content_header[0])
# print(content_rows)
for row in content_rows:
    print(row)

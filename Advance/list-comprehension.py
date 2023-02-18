# List comprehension: They are a shorter version of a list declaration, it is used to fitlration
my_list = ["Delia", "Francisco", "Victor", "Maria", "Maria", "Luis"]

new_list = [element for element in my_list if element != "Maria"]

print(my_list)
print(new_list)

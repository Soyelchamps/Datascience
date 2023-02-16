# Sets: They are unordered, unchangeable, unindexed and they can not accept duplicated values. It is case sensitive.

setExample = {"e1", "e2", "e3", "e4", "e1"}

print(setExample)
print(type(setExample))
setExample.add("E5")
setExample.add("E6")
setExample.add("E7")
setExample.add("E6")
print(setExample)

for i in setExample:
    print(i)

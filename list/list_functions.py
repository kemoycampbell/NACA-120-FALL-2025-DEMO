#we start with a empty list
names = []
print("The list is", names)

#add some names to the list
names.append("Nathan Clone")
names.append("Ahmed")
print("The list is", names)

#add a name at a specific position in the list
names.insert(0, "Nathan OG")
print("The list is", names)

#deleting Nathan Clone from the list
names.remove("Nathan Clone")
print("The list is", names)

#remember -1 mean remove at the last
#with pop, you must pass an index that you want to remove
# if you choose not to pass any index, it will default to -1
removed_name = names.pop(0)
print("The list is", names)
print("The removed name is:", removed_name)

#add kemoy and analiese
names.append("@@@@")
names.append("aaron")
names.append("Kemoy")
names.append("Analiese")
names.append("Kemoy###$$$!!!@@")
print("The list is", names)
#sort the list in a-z
names.sort()
print("The list is", names)

#sorting in z-a
#2 ways
# names.sort(reverse=True)
names.reverse()
print("The list is", names)


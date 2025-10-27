#example of empty list
# names = [] 
# print("The list is", names)

#example of list with some names
names = ["Nathan Clone", "Ahmed", "Nathan OG"] 
print("The list is", names)
print("The size of the list is", len(names))

#this will take the name from the index 0
# in the names list and assign it to the 
#variable nathan_clone
nathan_clone = names[0]
print("The name at index 0 is", nathan_clone)

#many options to get the last name
#you can use any
# last_name = names[len(names)-1]
last_name = names[2]
# last_name = names[-1]
print("The last name in the list is", last_name)

#swap nathan clone and ahmed
names[0] = "Ahmed"
names[1] = "Nathan Clone"

print("The list is", names)

#show all names in the list with a loop
#many ways
#using index
for index in range(len(names)):
    print("index:" + str(index) + "-->" + names[index])

#using for <variable> in names
print("\nNames\n======")
for name in names:
    print(name)
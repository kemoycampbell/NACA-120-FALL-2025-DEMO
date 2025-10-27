names = []

while True:
    name = input("Enter a name:")
    names.append(name)
    print(name+" was added to the list")
    again = input("Do you want to add another name? (Y/N)")
    if again == "N":
        break

#show all names that was added
print("Names\n=====")
for name in names:
    print(name)
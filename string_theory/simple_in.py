name = "Kemoy"
target  = "e"


found_match = False
for letter in name:
    if letter == target:
        found_match = True
        break


if found_match:
    print(f"A match for {target} was found in {name}")
else:
    print(f"No match for {target} was found in {name}")

#shortcut!!!
if target in name:
    print(f"A match for {target} was found in {name}:: shortcut")
else:
    print(f"No match for {target} was found in {name}:: shortcut")
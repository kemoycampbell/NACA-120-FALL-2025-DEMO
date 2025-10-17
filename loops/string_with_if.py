name = input("Enter your name:")
backward = ""
for letter in reversed(name):
    backward+=letter

if backward!=name:
    print("Your name backward and front is not the same")
else:
    print("Wow, your name spell the same back and front")
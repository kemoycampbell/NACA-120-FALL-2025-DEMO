#prompt the user for their name
name = input("Enter your first name:")

#we will use this to concatenate all name backward
backward_name = ""

#loop through the letter in the name in reverse order
for letter in reversed(name):
    #concatenate each letter backward
    backward_name = backward_name + letter

#show the reverse of the name
print("Your name in reverse is:" + backward_name)
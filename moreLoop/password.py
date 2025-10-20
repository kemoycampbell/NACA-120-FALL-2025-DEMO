CORRECT_PASSWORD = "Shh$3cret"
password = ""

#we will repeat as long as the password doesnt match
#the correct password
while password!=CORRECT_PASSWORD:
    password = input("Enter the password:")
    if password == CORRECT_PASSWORD:
        print("Welcome Admin")
    else:
        print("Incorrect password")
CORRECT_PASSWORD = "Shh$3cret"

while True:
    password = input("Enter the password:")
    if password!=CORRECT_PASSWORD:
        print("Incorrect password!")
        continue # if the password is incorrect, go back to asking

    print("Welcome Admin")
    break
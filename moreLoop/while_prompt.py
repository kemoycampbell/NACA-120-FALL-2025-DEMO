done = False

#continue prompt the user as long as they are not done
while done == False:
    prompt = input("Are you done? (Y/N):")
    if prompt == "Y":
        done = True
        print("GoodBye!")
    else:
        print("Let us do this again!")

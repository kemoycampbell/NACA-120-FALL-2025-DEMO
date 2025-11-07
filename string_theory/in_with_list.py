names = ["Nathan", "Analiese", "Ahmed"]


while True:
    target = input("Enter the student to search for:")
    if target in names:
        print(f"A match for {target} was found!")
        again = input("Do you want to search again Y/N:")
        if again.capitalize() == "Y":
            continue
        else:
            break
    else:
        print("No match found")
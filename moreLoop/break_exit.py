EXIT_WORD = "EXIT"
word = ""

#the program will repeat as long as the word is not "EXIT"
while True:
    word = input("Enter a word(EXIT to quit):")
    if word == EXIT_WORD:
        break
    print("You typed:" + word)
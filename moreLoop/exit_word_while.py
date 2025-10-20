EXIT_WORD = "EXIT"
word = ""

#the program will repeat as long as the word is not "EXIT"
while word!=EXIT_WORD:
    word = input("Enter a word(EXIT to quit):")
    print("You typed:" + word)
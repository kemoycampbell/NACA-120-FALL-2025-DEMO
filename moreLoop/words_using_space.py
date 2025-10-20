sentence = input("Enter a sentence:")

word = ""
for letter in sentence:
    #we will keep adding to the word variable until we find a space
    #a space signal a different word is coming next
    if letter == ";" or letter ==" " or letter =="|":
        print(word)
        word = ""
    else:
        word= word + letter

print(word)
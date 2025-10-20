sentence = input("Enter the sentence:")
target = input("Enter the word you would like to search for:")

#assume the word doesnt exist
hasWord = False

#loop through all words in the sentence
words = sentence.split(" ")
for word in words:
    if target == word:
        print("A match was found")
        hasWord = True

#show match not found if nothing was found
if hasWord == False:
    print("No match for " + target+ " was found")

sentence = input("Enter a sentence:")

words = sentence.split(" ")

print("show the words")
print(words)
print("total words:" + str(len(words)))

print("Looping through the words:")
for word in words:
    print(word)


#searching for a specifc match in a word
for word in words:
    if "Hello" == word:
        print("Hello is in the sentence")
#ask the user to type in a sentence
sentence = input("Enter a sentence:")
#ask the user what they want to search for
target = input("Enter the word you would like to search for:")

#setup the delimeter
delimeter = " "
#break up the sentence into a group of words
words = sentence.split(delimeter)

#setup a variable to track all matches we found
count = 0

#now go through all words and search for the match
for word in words:
    #do we find a match(yes)
    if target ==  word:
        count+=1 #increase the counter

#Show how many match we found
print("The word " + target+ " appeared in the sentence " + str(count) + " time(s)")


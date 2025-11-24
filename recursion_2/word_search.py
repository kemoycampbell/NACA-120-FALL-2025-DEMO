# A list of 20 words we will search through
words = [
    "apple", "banana", "cherry", "dragon", "elephant",
    "forest", "galaxy", "horizon", "island", "jungle",
    "kangaroo", "library", "mountain", "notebook", "ocean",
    "pyramid", "quantum", "river", "sunrise", "tornado"
]

# This function uses a loop to look for a word
def search_loop(word_list, target_word):
    # Go through each word in the list
    for word in word_list:
        # Check if the current word matches the word we want
        if word == target_word:
            return word  # Found it
    
    # If we finish the loop and did not find the word
    return -1

print(f"Loop found: {search_loop(words, 'apple')}")
print(f"Loop not found: {search_loop(words, 'yolo')}")


# This function searches using recursion (calling itself again and again)
def search_rec(words_list, target):
    # If the list is empty, the word is not here
    if len(words_list) == 0:
        return -1
    
    # Look at the first word in the list
    word = words_list[0]

    # If the first word matches, return it
    if word == target:
        return word

    # Call the function again but skip the first word
    return search_rec(words_list[1:], target)

print(f"search_rec found: {search_rec(words, 'apple')}")
print(f"search_rec not found: {search_rec(words, 'yolo')}")


# This version uses recursion but also keeps track of the index
def search_rec_index(words_list, target, index):
    # If index is negative, it is not valid
    if index < 0:
        return -1

    # If index is past the end of the list, stop searching
    if index >= len(words_list):
        return -1
    
    # Get the word at the current index
    word = words_list[index]

    # Check if this word is the one we want
    if word == target:
        return word
    
    # Move to the next index and search again
    return search_rec_index(words_list, target, index + 1)

print(f"search_rec_index found: {search_rec_index(words, 'apple', 0)}")
print(f"search_rec_index not found: {search_rec_index(words, 'yolo', 0)}")

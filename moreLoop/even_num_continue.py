MAX_NUMBER = 30
current_number = 0


#we want to count from current number to max number(inclusive)
while current_number <= MAX_NUMBER:
    current_number+=1
    #is even?
    if current_number % 2 != 0:
        continue
    print(current_number)
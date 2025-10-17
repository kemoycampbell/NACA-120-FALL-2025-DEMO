#prompt the user for the start number
start = int(input("Enter the starting number:"))
#prompt the user for the stop number
stop = int(input("Enter the stopping number:"))


total = 0
#loop between start and stop range
for num in range(start, stop+1):
    #show every number from start - stop + 1
    print(num)
    #add up the total
    total = total + num

#show the total sum of all the numbers
print("The sum of " + str(start) + " to " + str(stop) +" is " + str(total))

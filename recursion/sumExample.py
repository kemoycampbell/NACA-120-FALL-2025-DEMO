def sumLoop(n):
    result = 0
    for num in range(1,n+1):
        result = result + num
    
    return result

def sumRec(n):
    #base case
    if n == 1:
        return 1
    
    #reduce by do n-1.. will approach 1
    #eventually
    next = n-1

    #we are trying to do the sum so we
    #take current n plus the next recurive call(n-1)
    return n + sumRec(next)

def sumRec2(n):
    #base case, if we are at 10, we just return a 10
    if n == 10:
        return 10
    
    #we are approaching up so we add 1
    next = n + 1
    #we are trying to do the sum so we
    #take current n plus the next recurive call(n+1)
    return n + sumRec2(next)


print(f"The sum of 1 to 10(loop) is: {sumLoop(10)}")

print(f"The sum of 1 to 10 (Recursion) is: {sumRec(10)}")
print(f"The sum of 1 to 10 (Recursion2) is: {sumRec2(1)}")


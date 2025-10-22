def factorial(number):
    result  = 1
    #we fix this by do +1
    for i in range(1,number+1):
        result = result * i
    return result

def main():
    num = int(input("Enter a number to find its factorial value:"))
    res = factorial(num)
    print(str(num)+"!="+str(res))

main()
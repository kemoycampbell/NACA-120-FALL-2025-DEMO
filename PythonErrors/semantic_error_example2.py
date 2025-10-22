def factorial(number):
    result  = 1
    #the issue here is that range do from 1-(number-1)
    #aka number is not included and we want it to!
    for i in range(1,number):
        result = result * i
    return result

def main():
    num = int(input("Enter a number to find its factorial value:"))
    res = factorial(num)
    print(str(num)+"!="+str(res))

main()
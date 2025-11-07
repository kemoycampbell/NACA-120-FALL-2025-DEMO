name = "Analiese"
age = 100
major = "retired!"

#the old way "concatenation"
string_in_a_variable = "Hello my name is " + name + ". I am "+ str(age) + " and I am "+ major
print("Hello my name is " + name + ". I am "+ str(age) + " and I am "+ major)
print(string_in_a_variable)

#using f string
string_in_a_variable = f"Hello my name is {name}. I am {age} and I am {major}"
print(f"Hello my name is {name}. I am {age} and I am {major}")
print(string_in_a_variable)

#string format
string_in_a_variable = "Hello my name is {0}. I am {1} and I am {2}".format(name,age,major)
print("Hello my name is {0}. I am {1} and I am {2}".format(name,age,major))

print(string_in_a_variable)

#string with format controls
print("Hello my name is %s. I am %d and I am %s"%(name,age,major))

price = 100.999999
product = "lame Iphone s v0"
print("The price of the product %s is price %.3f" % (product, price))



import re

pattern = r'\d+'
text = "Hello world my name is Kemoy, I am 12! and I think I want to be 55"

result = re.search(pattern, text)
if result == None:
    print("No match for the pattern found!")

print(result.group())

print("\n==============")
print(".match")

pattern = r'\d+'
text = "12 is a number"
result = re.match(pattern, text)

if result == None:
    print("The string doesnt start with a number")
else:
    print(result.group())



print("\n================\nfindall")
pattern = r'\(?\d{3}\)?\s?-?\d{3}-\d{4}'
text = "Call Alice at 555-123-4567 or Bob at (212) 555-7890. Urgent issues can go to support at 800-555-0000."

result = re.findall(pattern, text)

if not result:
    print("There are no phone numbers")
else:
    print(result)

    for number in result:
        print(number)


print("\n=================\nre.sub")
text =  "000-14-6894"
pattern = r'\d{3}-?\d{2}-?'
replace_with="***-**-"
last_four_ssn = re.sub(pattern, replace_with, text)

print(f"Your full ssn is: {text} and Your last 4 ssn is:{last_four_ssn}")


def is_digit(text):
    







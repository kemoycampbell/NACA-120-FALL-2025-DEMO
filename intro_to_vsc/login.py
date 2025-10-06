"""
Author: Kemoy Campbell
Date: 10/06/2025
Purpose:
    This program prompts the user for a password.
    If the password is correct, a welcome admin is display
    otherwise show error
"""



CORRECT_PASSWORD = 'topS3cret'
password = input("Enter the password:")

#compare and check if the password is right
if password == CORRECT_PASSWORD:
    #show welcome admin if right password
    print("Welcome admin")
else:
    #show error if wrong password
    print("Incorrect username or password")

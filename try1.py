import random, my_functions

options = '''
1 for cipher
2 for collatz
'''
user_input = int(input(options))

if user_input == 1:
    response = input("type your message: ").lower()
    # TODO call the cipher function
elif user_input == 2:
    num = int(input("Type your number: "))
    # TODO call the collatz function


# checking the docstrings

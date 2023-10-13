# Write a program that stores a number and the user has to figure it out
# The user can input guesses
# After each guess the program would tell one of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
a = int(input("please insert your number: "))
b = 8
if a > b:
    print("The stored number is higher")
elif a < b:
    print("The stored number is lower")
elif a == b:
    print("You found the number")
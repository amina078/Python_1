# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
a = int(input("Please insert the number: "))
for i in range (1, a + 1, 2):
    space = a - i
    print(" " * space, "*" * (2 * i - 1))
for n in range (a, 0, -2):
    space = a - n
    print(" " * space, "*" * (2 * n - 1))
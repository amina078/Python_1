# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%
#
# The square should have as many lines as the number was
a = int(input("Please insert the number: "))
print("%" * (a + 1))
for i in range (1, a):
    print("%"," " * (a - 3),"%")
print("%" * (a + 1))
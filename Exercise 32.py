# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = int(input("Please insert the number: "))
print("%" * (a))
for i in range (2,a -1):
    c = i - 1
    d = (a - 1) - i - 1
    print("%" +(" " * c) + "%" + (" " * d) + "%")
print("%" * (a))
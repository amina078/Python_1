# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5
number_1 = int(input("Please type your first number: "))
number_2 = int(input("Please type your second number: "))
if number_2 < number_1:
    print("The second number should be bigger!")
else:
    for i in range(number_1, number_2):
        print(i)
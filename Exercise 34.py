# Write a program that asks for a number
# It would ask this many times to enter an integer
# If all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4
count = int(input("Please insert the count of numbers "))
sum_of_numbers = 0
for counter in range(count):
    number = int(input("Please insert next number: "))
    sum_of_numbers = sum_of_numbers + number
print(f"Sum: {sum_of_numbers}")
print(f"Average: {sum_of_numbers / count}")
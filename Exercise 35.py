# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
number_input = int(input("Please type a number: "))
for i in range (0, number_input):
    if i % 2 == 0:
        print(" ","% " * number_input)
    else:
        print("% " * number_input)  

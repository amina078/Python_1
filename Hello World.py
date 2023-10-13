# Exercise 1
print ("Hello, World")
# Exercise 2
print("Humpty Dumpty sat on a wall,")
print("Humpty Dumpty had a great fall.")
print("All the king's horses and all the king's men")
print("Couldn't put Humpty together again.")
# Exercise 3
print ("Hello, Parsa")
print ("Hello, Lamis")
print ("Hello, Tamas")
# Exercise 4
print ("Amina Shermatova")
print ("23")
print ("1.70")
# Exercise 5
print (13 + 22)
print (22 - 13)
print (22 * 13)
print (22 / 13)
print (22 // 13)
print (22 % 13)
# Exercise 6
x = 17 * 5 
print(x)
y = x * 6
print (y)
a = 52 * 17
print(a)
b =  y / a
print (b)
percentage = b * 100
print (percentage)
# Exercise 7
my_fav = 7
print("My Favorite number is : " + str(my_fav))
# Exercise 8
a , b = 123 , 526
a , b = b , a
print (f"Number b: {b}")
print (f"Number b: {a}")
# Exercise 9
massinKG = 81.2
heightinM = 1.78 ** 2
print (massinKG/heightinM)
# Exercise 10
name = "Amina"
print (f"My name is : {name}")
age = 23
print (f"My age : {age}")
height = 1.70
print (f"My height : {height}")
single = True
print(single)
# Exercise 11
q = 3
q += 10
print (q)
w = 100
w -= 7
print(w)
e = 44
e *= 2
print (e)
r = 125
r /= 5
print (r)
t = 8 #create a variable
t_cubed = t ** 3 # fixed the cube
print (t_cubed)
f1 = 123
f2 = 345
if f1 > f2:
    print("f1 is greater than f2")
else:
    print("f2 is greater")
g1 = 350
g2 = 200
g2_double = g2 * 2
if g2_double > g1:
    print("g2 is greater than g1")
else:
    print("g1 is greater")    
h = 1357988018575474
h_divisor = h % 11 #% sign gives back the remaining
if h_divisor == 0:
    print("h can be divided by 11")
else:
    print("h cannot be divided by 11")
i1 = 10
i2 = 3
i2_squared = i2 ** 2
i2_cubed = i2 ** 3
if i1 > i2_squared and i1 < i2_cubed:
    print ("i1 is higher than i2 squared and smaller than i2 cubed")
else:
    print ("false")
j = 1521
j_disible_5= j % 5
j_disible_3= j % 3
if j_disible_5 == 0 or j_disible_3 == 0:
    print ("is divisible by 3 or 5")
else:
    print ("is not divisible by 3 or 5")
# Exercise 12
l = 5.5
h = 5.2
w = 2.7
volume = l * h * w
print (f"volume {volume}")
surface_area = h * w * 2 + l * h * 2 + l * w *2
print (f"surface_area {surface_area}")
# Exercise 13
current_hours = 14
current_minutes = 34
current_seconds = 42
seconds_inaday = 24 * 60 * 60
remaining_seconds = seconds_inaday - ((current_hours * 60 * 60 ) + (current_minutes * 60) + current_seconds)
print (f"remaining seconds : {remaining_seconds}")
# Exercise 14
name_input = input ("please enter your name: ") #promt text that the user follows
print(f"Hello, {name_input}")
# Exercise 15
miles = int(input ("please enter the miles: ")) #int was used to integer the nest it 
km = miles * 1.609344
print(f"miles: {km}")
# Exercise 16
number_of_chicken= int(input ("please enter how many chickens you have: "))
number_of_pigs= int(input ("please enter how many pigs you have: "))
legs = number_of_chicken * 2 + number_of_pigs * 4
print(f"Animal legs: {legs}")
# Exercise 17
number_1 = int(input("enter a number :"))
number_2 = int(input("enter another number :"))
number_3 = int(input("enter a third number :"))
number_4 = int(input("enter a fourth number :"))
number_5 = int(input("enter a fifth number :"))
sum = number_1 + number_2 + number_3 + number_4 + number_5
average = sum / 5
print(f"Sum of numbers: {sum}, Average of numbers: {average}")
# Exercise 18
number_input = int(input ("please enter the number: "))
if number_input % 2 ==0:
    print("The number is even")
else:
    print("The number is odd")
# Exercise 19
standardnumber_input = int(input ("please enter the number: "))
if standardnumber_input <= 0:
    print("Not enough")
elif standardnumber_input == 1:
    print("One")
elif standardnumber_input == 2:
    print("Two")
else:
    print("a lot")
# Exercise 20
biggernumber_input1 = int(input ("please enter the first number: "))
biggernumber_input2 = int(input ("please enter the first number: "))
if biggernumber_input1 < biggernumber_input2:
    print(f"This number is bigger: {biggernumber_input2}")
else:
    print(f"This number is bigger: {biggernumber_input1}")
# Exercise 21
input_girls = int(input ("please enter the number of girls that come to the party: "))
input_boys = int(input ("please enter the number of boys that come to the party: "))
number_of_people = input_girls + input_boys
if input_girls == input_boys and number_of_people >= 20:
    print("The party is excellent")
elif number_of_people >= 20 and input_girls != input_boys:
    print("Quite a cool party!")
elif number_of_people < 20 and input_girls > 0:
    print("Average party ... ")
elif input_girls == 0:
    print("Sausage party")
# Exercise 22
a = 24
output1 = 0 
if a % 2 == 0:
    output1 += 1
    print("output 1: ", output1 )
else :
    print("output 1: ", output1 )
b = 13
output2 = ""
if 10 < b and b > 20:
    print("Sweet")
elif 10 > b:
    print("Less")
elif b > 20:
    print("More")
else:
     print(output2)
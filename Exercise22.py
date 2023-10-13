a = 24
output1 = 0 
if a % 2 == 0:
    output1 += 1
    print("output 1: ", output1 )
else :
    print("output 1: ", output1 )
#part2
b = 13
output2 = ""
if 10 < b and b < 20:
    output2 = "Sweet"
    print(output2)
elif 10 > b:
    output2 = "Less"
    print(output2)
elif b > 20:
    output2 = "More"
    print(output2)
else:
    print(output2)
#part3
c = 123
credits = 100
is_bonus = False
if credits > 50 and is_bonus == False:
    print(c - 2)
if credits < 50 and is_bonus == False:
    print(c - 1)
if is_bonus == True: 
    print (c)
#part4
d = 8
time = 120
output3 = ""
if d % 4 == 0 and time < 200:
    output3 = "check"
    print(output3)
elif time > 200:
    output3 = "Time out"
    print(output3)
else:
    output3 = "Run forest Run!"
    print(output3) 
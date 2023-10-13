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
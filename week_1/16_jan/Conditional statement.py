if 4<40:
    print("4 is less than 40")

#____________________________________________

if 10>=10:
    print("10 is greater than or equal to 10")
else:
    print("10 is not less than or equal to 10")


#____________________________________________

x,y,z=10,20,30

if x>y and x>z:
    print("x is the greatest")
elif y>x and y>z:
    print("y is the greatest")
else:
    print("z is the greatest")

#_______________________________ nested conditions

if x>y:
    if x>z:
        print("x is higher")
    if y>z:
        print("y is mid and z is low")
elif y>z:
    print("y is higher")
    if z>x:
        print("z is mid and x is low")
else:
    if x>y:
        print("z is higher , x is mid and y is lower")
    else:
        print("z is higher , y is mid , x is lower")



#____________________________________________ not keyword in loop

if not 10>1:
    print("okay this is not expected")
else:
    print("okay this is  expected")

#___________________________________________ or and and key word

if 10>100 or 1>0:
    print("this is true")
else:
    print("this is false")

if 10>100 and 20>100:
    print("10>100 and 20>100")
else:
    print("both or one of condition is wrong")

#____________________________________________

if 10>2:
    pass
else:
    print("this is not pass")


#____________________________________________
a,b=10,20

print("a>b") if a>b else print("b>=a")
# _______________________variables_______________________________

# variables: Variables are containers for storing data values.

"""
vatiable name:

-> A variable name must start with a letter or the underscore character
-> A variable name cannot start with a number
-> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
-> Variable names are case-sensitive (age, Age and AGE are three different variables)
-> A variable name cannot be any of the Python keywords.

"""

x = 100  #  here x is variable and 100 is value that assign to x

s1 = "ummed"
s2 = "choudhary"
s3 = """hello my 
        name is ummed"""

print(s1 + s2)
print(s1, s2)

s4 = s1 + s2
print(s4)

# get the data type
print(type(10))
print(type("ummed"))
print(type(True))


# casting

a = "100"
print(type(a))
a = int(a)
print(type(a))

a = 10.10
print(type(a))
a = int(a)
print(type(a))

b = 5
print(type(b))
b = float(b)
print(type(b))

ls = [1, 2, 3]
print(type(ls))
tup = tuple(ls)
print(type(ls))

# Case-sensitive

N = 10
n = 100
if n == N:
    print("n and N is same")
else:
    print("both are diffrent")


# one to multi variable

a = b = c = 100

print(a)
print(b)
print(c)

# many to many
x, y, z = 1, 2, 3

print(x, y, z)


# global variable: variable which not declared inside any function

zc = 100  # global variable


def func():
    zc = 20  # local variable
    print(zc)


print(zc)  # output will be 100


var = "local"


def func1():
    global var  # access of global variable inside a function
    var = "global"


func1()
print(var)


# _____________________________dataTypes_________________________________

x = 100  # int
print(type(x))
x = 10.5  # float
print(type(x))
x = "ummed"  # string
print(type(x))
x = 10j  # complex
print(type(x))
x = True  # bool
print(type(x))
x = False  # bool
print(type(x))
x = [1, 2, 3]  # list
print(type(x))
x = (1, 2, 3)  # tuple
print(type(x))
x = {1, 2, 3}  # set
print(type(x))
x = {"1": "100"}  # dictionaxry
print(type(x))
x = range(10)  # range
print(type(x))

x = None  # none
print(type(x))
x = bytearray(5)  # bytearray
print(type(x))

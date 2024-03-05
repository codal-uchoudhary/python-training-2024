# _________________________________________staticMethods_________________________________
"""
 staticmethod:- this is a method takes neither a self nor a cls parameters
 that's why static method neither modify object state nor class state.

"""
# staticmethod:- this is a method takes neither a self not a cls parameters


class demo:
    def __init__(self, a):
        self.num = a

    @staticmethod
    def sum(a, b):
        return a + b


print(demo.sum(1, 2))  # i can use staticmethods without using instance of class

obj_demo = demo(10)
print(obj_demo.sum(10, 20))


# ______________________________________classmethods_______________________________________

"""
classMethods: class method take a cls parameter instead of self, that points
to the class and not the object of a class.

and it can't modify object instance of class , because it has no access to instance of class
q
 
"""


class demo2:
    company = "Apple"
    location = "new-york"

    def show(self):
        print(self.company)
        print(self.location)

    @classmethod
    def changeCompany(cls, name):
        cls.company = name


obj01 = demo2()
obj02 = demo2()

obj01.company = "c01"
obj02.company = "c02"

print(obj01.company)
print(obj02.company)
print(demo2.company)

obj01.changeCompany("tesla")

print(obj01.company)
print(obj02.company)
print(demo2.company)

demo2.changeCompany("tesla2")

print(obj01.company)
print(obj02.company)
print(demo2.company)

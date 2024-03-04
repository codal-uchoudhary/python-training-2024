# class : class is a counstructor for creating an object , so class acts like blueprint
# object : object is an instance of a class

# _________________________________create a class_______________________________


class person:
    # data members (variables)
    # methods      (functions)

    pass  # pass keyword is use when we don't know the defination of class at moment


# ______________________________init() function __________________________________

# __init__() is a constructor of a class , the function which is executed automatically when an object of class is created
# __init__() function is used to initialize an object

# self : self parameter is reffrence to the current instanse of a class , which is used to access the variable of a class


class person1:
    # data members
    name = None
    gender = None
    color = None
    age = None

    def __init__(self, name, gender, color, age):
        print("the object is created")
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

    # methods

    def info_of_person(self):
        print("name is", self.name)
        print("age is ", self.age)
        print("color is ", self.color)
        print("gender is ", self.gender)


# ________________________________create_an_object___________________________________


abhay = person1("abhay", "male", "brown", 30)

abhay.info_of_person()

# Modify object data members


abhay.age = 35
abhay.color = "white"

abhay.info_of_person()

del abhay.gender

abhay.info_of_person()


# ______________________________________str__() function___________________


# __set__() return an string as a result when an object is created
class demo:
    age = 20

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"age is {self.age} and name is {self.name}"

    def dob(self):
        self.color = "red"


ume = demo("ummed")

print(ume.age)
print(ume)  # return an string due to __set__() function
print(abhay)
print(ume.name)
print("color is ", ume.color)  # not accesible local data member

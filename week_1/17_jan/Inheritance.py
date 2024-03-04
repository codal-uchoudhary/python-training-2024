# inheritance: inheritance allow us to define a class that inheritance all the methods and data from parent class


class car:  # parent class
    def __init__(self, company):
        self.wheels = 4
        self.type = "pasanger"
        self.capacity = 5
        self.company = company
        print("car func is executed")

    def info(self):
        print(
            "wheels is",
            self.wheels,
            " type is ",
            self.type,
            " capacity is ",
            self.capacity,
            "  : ",
            self.company,
        )


class ford(car):  # child class decleration
    def __init__(self, color, modal, year, comnany):
        super().__init__(
            comnany
        )  # super method is used to call parent __init__() func in child class
        self.color = color
        self.year = year
        self.modal = modal
        print("ford func class is executed")

    def info_c(self):
        print(self.color, self.modal, self.year)
        print(self.wheels)


mustang_m1 = ford("black", "mustang", 1990, "ford")  # child class ob]ject

mustang_m1.info_c()  # method from child class

mustang_m1.info()  # method from parent class


# ___________________________________multilevel inheritance___________________________________


class figo(ford):
    def __init__(self, state, price, color, modal, year, company):
        super().__init__(color, modal, year, company)
        self.state = state
        self.price = price
        print("figo func class is executed")

    def info_cc(self):
        print(self.wheels)
        print(self.company)
        print(self.color)
        print(self.modal)
        print(self.price)
        print(self.state)


figo_f1 = figo("raj", 400000, "red", "figo", 2020, "ford")

figo_f1.info_cc()


# ____________________________________________multiple inheritance____________________________________


class father:
    fatherName = "p"

    def __init__(self, fname):
        self.fatherName = fname
        print("father class")

    def fathername(self):
        print("father name is ", self.fatherName)


class mother:
    motherName = "m"

    def __init__(self, mname):
        self.motherName = mname
        print("mother class is executed")

    def mothername(self):
        print("mother name is ", self.motherName)


class child(father, mother):
    def __init__(self, name):
        # father.__init__(f)
        # mother.__init__(m)
        self.childName = name
        print("child class is executed")

    def sayMyName(self):
        print("my name is", self.childName)
        print(self.fatherName)
        print(self.motherName)


# ume = child('u','p','m')
ume = child("u")
ume.fathername()
ume.mothername()

ume.sayMyName()


# __________________________________________ daimond problem________________________


class person:
    def display(self):
        print("person")


class father(person):
    def display(self):
        print("father")


class mother(person):
    def display(self):
        print("mother")


class child(father, person):
    pass


# now let's find the order of class in thid daimond shape

print(child.__mro__)

# we can see that father comes before mother in he order ,so father methods first invoke

ume = child()

ume.display()


# create new class with different order


class child2(mother, father):
    pass


child2 = child2()

child2.display()
# output will "mother" because order is change , now class mother invoke first

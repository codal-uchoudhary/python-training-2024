
# incapsulation : encapsulation  allow us to hide or protect our class members

# incapsulation do not provide direct access to data members

# types of data member

# 1> protected :- those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses.

# 2> private :- those members of class that only accessed within the class

# 3> public :- those members which can be accesses from any where within the file



class maths:

    def __init__(self):
        self.num1 = 10
        self.num2 = 20

    def add(self,x,y):
        return x+y

class base(maths):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def plus(self):
        return self.add(self.x,self.y)

    def get_nums(self):
        maths.__init__(self)
        self.num2 = 30
        return self.num2


obj_base = base(1,2)

print(obj_base.plus())
print(obj_base.get_nums())




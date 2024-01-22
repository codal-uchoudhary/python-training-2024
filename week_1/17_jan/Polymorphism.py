

# polymorphism : polymorphism means many forms it refers to methods , functions , oprators, with same name that can be
# executed on many objects

# class polymorphisms : Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class demo:

    def add(self,x,y):
        print("class demo")
        return x+y


    def add(self,x,y):    # this function is override the privious function
        print("overided")
        return x-y


class child(demo):

    def add(self,x,y):
        print("class child")
        return x*y

class child2(demo):
    pass


demo_obj = demo()
print(demo_obj.add(1,2))




child_obj = child()
print(child_obj.add(1,2))



child2_obj = child2()
print(child2_obj.add(1,2))


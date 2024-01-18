# decoratores : using dacoratores we can add extra features to the function withod changing the original function

# using dacorators withod syntax suger

def div(x,y):
    return x/y

def smart_math(func):

    def result(x,y):
        if y>x:
            x,y = y,x
        return func(x,y)

    return result

div = smart_math(div)

print(div(2,1))





# use syntax suger (@)

@smart_math
def sub(x,y):
    return x-y

def sub2(x,y):
    return x-y

print(sub(1,2))
print(sub2(1,2))


#__________________________args and kwargs__________________

# *args: non keywords arguments

def add(*i):
    c=0
    for j in i:
        c +=j
    return c

print(add(1,2,3,4,5))


# **kwargs : arguments with key words

def multi(**kwargs):
    i=1;
    for j in kwargs.values():
        i *=j
    return i



print(multi(a=1,b=2,c=3))




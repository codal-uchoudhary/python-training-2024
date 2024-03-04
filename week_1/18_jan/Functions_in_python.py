# ____________________________________Treating the functions as object_______________


def double(x):
    return x * 2


def square(x):
    return x * x


print(double(2))

demo = double

print(demo(10))

# ____________________________________passing the function as an argument_________________


def math(func, x):
    return func(x)


print(math(demo, 20))
print(math(square, 20))

# _________________________running funciton from another function_____________


def bigFunc(x):
    def multi(y):
        return x * y

    return multi


a = bigFunc(10)

print(a(20))

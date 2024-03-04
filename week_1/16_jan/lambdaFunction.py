# labda functin: A lambda function is a small anonymous function.

# basic syntax

x = lambda a, b: a + b
print(x(10, 20))

# labda on list

list1 = [1, 2, 3, 4]


def multi_n(n):
    return lambda i: i * n


for i in range(len(list1)):
    x = multi_n(10)
    list1[i] = x(list1[i])

print(list1)

for i in range(len(list1)):
    x = multi_n(1000)
    list1[i] = x(list1[i])

print(list1)


# lambda on dictionary

dict1 = {"a": 1, "b": 2, "c": 3}

for i in dict1:
    x = multi_n(2)
    dict1[i] = x(dict1[i])
    print(dict1[i])

print(dict1.values())

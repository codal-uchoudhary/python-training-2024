from collections import OrderedDict

# orderedDict : orderedDict allow us to control the order of itmes in dictionaries

myDict = OrderedDict()

myDict[1] = 100
myDict[2] = 200
myDict[3] = 300
myDict[4] = 400
myDict[5] = 500

for i in myDict.items():
    print(i)

# both loop will give the same order

for i in myDict.items():
    print(i)


print(type(myDict))

demo = {1: 10, 2: 20, 3: 30}

demo = OrderedDict(demo)

print(type(demo))

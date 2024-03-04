from collections import defaultdict

"""

defaultdict: is the subdivision of the dict class. Its importance lies in the 
fact that it allows each new key to be given a default value based on the type 
of dictionary being created.

we can give three default values = list,set,int

so , default dict will not give any key-error if particular key is not exist 
in default dict

"""


# dictionary

demod = dict()
# print(demod["1"])   // gives error


# default dict

defaultDictDemo_1 = defaultdict(int)
print(defaultDictDemo_1[1])

defaultDictDemo_2 = defaultdict(list)
print(defaultDictDemo_2["20"])

defaultDictDemo_3 = defaultdict(set)
print(defaultDictDemo_3[9])


# lets assign a value

defaultDictDemo_1["one"] = 1
defaultDictDemo_1["two"] = 2
defaultDictDemo_1["three"]
print(defaultDictDemo_1["one"])
print(defaultDictDemo_1["two"])
print(
    defaultDictDemo_1["three"]
)  # give zero because this key does not assign any value


defaultDictDemo_2[1] = [1]
defaultDictDemo_2[2] = [2]
defaultDictDemo_2[3] = 3000

print(defaultDictDemo_2[1])
print(defaultDictDemo_2[2])
print(defaultDictDemo_2[3])
print(defaultDictDemo_2[4])

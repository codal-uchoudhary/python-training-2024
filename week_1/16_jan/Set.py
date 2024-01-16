# set: A set is a collection which is unordered, unchangeable*, and unindexed.

set1 = {0,1,2,3,4,5,1,2}  # duplicate values are not allowed in sert

print(type(set1))
print(set1)

# true == 1 and false == 0

set2 = {1,2,3,True}
set3={False,0,2,3}

print(set2)
print(set3)

#  len() function in set gives the length of set

print(len(set3))

# set() constructor

list1 = [1,2,3]

set4 = set(list1)
print(type(set4))

#________________________loop in set____________________________

for i in set1:
    print(i)

#____________________check item in set________________________

if 100 in set1:
    print("100 is present in set1")
else:
    print("100 is not present in set1")


#_____________________add or remove items in set____________________

set5 = {1,2,3,4,5}

set5.add(6)

print(set5)

s1 = {'a','b'}
set5.update(s1)

print(set5)
list1 = [100]
set5.update(list1)
print(set5)

# remove() method

set5.remove(100)  # this method will give error if item does not exist
print(set5)

# discard() method

set5.discard(1)
print(set5)  # this method never give error if item dorst not exit

# pop() method

set5.pop() # this method will remove item randomly

print(set5)

set5.clear()
print(set5)

del set5  # set5 is deleted

#________________________________join two set________________________

# union() method
s1 = {1,2,3}
s2 = {2,3,4,5}

s3 = s2.union(s1)  # return new set
print(s1)
print(s2)
print(s3)

# update() method
s1.update(s2)   # add items from one set to another

print(s1)
print(s2)

#intersection() method

x = {1,2,3,4,5}
y = {4,5,6,7}

z = x.intersection(y)
print(z)

# intersection_update() method

x.intersection_update(y)  # keep only the items that are present in set
print(x)

# symmetric_diffrence_update() method

a = {1,2,3,4,5}
b = {3,4,5,6,7}

c = a.symmetric_difference(b)
print(c)

a.symmetric_difference_update(b)
print(a)



#___________________________________Time complexity in set______________________

# Time complexity to find a item in  a set is O(N)
# Time Complexity to traverse a set is O(N)



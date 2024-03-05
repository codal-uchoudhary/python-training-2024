# this file contain the code and concepts of list and python

# List is a collection which is ordered and changeable. Allows duplicate members.

# create list

myList = [1, 2, 3, 4, 5]
myList2 = ["a", "b", "c"]
myList3 = [1, 2, 3, "a", "b"]
myList4 = [True, "a", 2.5, 1, "name"]

# print the list

print(myList4)

# check data type of list

print(type(myList4))

# list allow duplicates items

duplicate_items_in_list = [1, 1, 2, 2, 3, 3]
print("duplicate items in list", duplicate_items_in_list)

# get length of list using len() fun

print(myList, " The length of the list is:", len(myList))

# list constructot: another methos to create a list

newList = list((3, 2, 1))
print(type(newList))


# _______________________Access list items____________________________

myList5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(myList5[0])
print(myList5[4])

print(myList5[-1])
print(myList5[-2])
print(myList5[-3])

# range of index
print(myList5[0:5])
print(myList5[:5])
print(myList5[5:])
print(myList5[:])

print(myList5[-3:-1])
print(myList5[-3:])  # 8 9 10
print(myList5[:-5])  # 1,2,3,4,5
print(myList5[1:-3])  # 2,3,4,5,6,7
print(myList5[-5:])
print(myList5[-1:-3])  # travelsal in wrong direction

# check if item exists

if 1 in myList5:
    print("1 is present in mylist5")
if 100 not in myList5:
    print("100 is not present in mylist5")

# __________________________________change list items_______________________________

myList6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myList6[0] = 10
myList6[-1] = 100

print(myList6)

myList6[1:5] = [20, 30, 40, 50]
print(myList6)

myList6[5:6] = [6, 6.2, 6.8]
print(myList6)
print("done")
myList6[5:8] = [6]
print(myList6)

myList6.insert(2, -3)
print(myList6)

# ____________________________________add list items_____________________________

myList6.append(11)
print(myList6)

myList6.extend([12, 13, 14, 15])
print(myList6)

l1 = [16, 17]

myList6.extend(l1)
print(myList6)
# we can add tuple , dic,set using extends method
t1 = (18, 19, 20)
d1 = {21, 22}

myList6.extend(t1)
myList6.extend(d1)

print(myList6)

# ____________________________________________ remove list tems_____________________________

list7 = [1, 2, 3, 4, 5]

list7.remove(5)  # remove specified item
print(list7)
list7.pop()  # pop remove the last item
print(list7)
list7.pop(0)  # pop also remove the item on specific index
print(list7)
del list7[0]
print(list7)

del list7  # list deleted

list7 = [9, 8, 7]

list7.clear()
print(list7)

# ___________________________________loop through list______________________________

list8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list8:
    print(i)

n = len(list8)

for i in range(n):
    print(list8[i])

# short hand
print("short hand way")
[print(x) for x in list8]

# __________________________________sorting on list__________________________

list9 = [3, 5, 1, 2, 6, 7]
list9.sort()
print(list9)
list9.sort(reverse=True)
print(list9)

list10 = ["a", "A", "b", "B", "c", "C"]
list10.sort()
print(list10)
list11 = ["a", "A", "c", "C", "b", "B"]
list10.reverse()
print(list10)

listx = []
listy = [1, 2, 3]
listx = listy


# ________________________________________copy of list_______________


# simple copy of list

print(listx)
print(listy)

listy[0] = 100
print(listx)
print(listy)

# deep copy of list

x = []
y = [1, 2]
x = y.copy()
y[1] = 200

print(x)
print(y)


# ________________________________________join two list__________________

ll1 = [1, 2, 3]
ll2 = [4, 5, 6]

ll3 = ll1 + ll2
print(ll3)

ll2.extend(ll1)
print(ll2)

ll1 = ll1 + ll2
print(ll1)


# ________________________________List Comprehension_________________________________

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# now we want a list with only even number

even_list = [i for i in list1 if i % 2 == 0]

print("even list is ", even_list)

greater_than_5 = [i for i in list1 if i > 5]

print(greater_than_5)


# condition is like filter that filter the items in a new list

# this work on any itrable data

less_than_5 = [i for i in range(10) if i < 5]

print(less_than_5)

tup = (1, 2, 3, 4, 5)

list_tup = [i for i in tup if not (i == 2 or i == 4)]

print(list_tup)

# Exression: expression work as the outcome of item from the itrable data

square = [i * i for i in tup]

print(square)

update_tup = [i if i != 1 else 10 for i in tup]

print(update_tup)

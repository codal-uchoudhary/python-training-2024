# Dictionaries : A dictionary is a collection which is ordered,
# changeable and do not allow duplicates.

dict1 = {"brand": "dell", "processor": "i7", "year": "2024"}

print(dict1)

print(dict1["brand"])
dict1["brand"] = "lenovo"

print(dict1["brand"])

# _____________________access item__________________________

# get() method

print(dict1.get("year"))

# key() method , return all the keys of dict

print(dict1.keys())

print(dict1.values())

print(dict1.items())


# ___________________add new items_______________________

dict1["color"] = "silver"

print(dict1)

if "color" in dict1.keys():
    print("color is key in dict1")
else:
    print("color is not present in dict1")

# _____________________change item__________________________

dict1["color"] = "black"
dict1.update({"year": "2024"})

print(dict1)

# ___________________add items______________________________

dict1.update({"country": "china"})
dict1["owner"] = "xyz"

print(dict1)

# _________________remove items___________________________

# pop() method

dict1.popitem()  # remove the last item in dict
print(dict1)

del dict1["country"]
print(dict1)

dict1.clear()
print(dict1)

del dict1  # dict1 is deleted forwver


# __________________________ loops in dict___________________________

dict2 = {1: 100, 2: 200, 3: 300}

for i in dict2:
    print(i)

for i in dict2:
    print(dict2[i])

for i in dict2.values():
    print(i)

for i, j in dict2.items():
    print(i, " : ", j)


# ___________________________copy of dict___________________________

dict3 = dict2.copy()
print(dict3)

dict4 = dict(dict2)
print(dict4)

# __________________________nested dict__________________________________

dictn = {"item1": {1: "a", 2: "b"}, "item2": {3: "c", 4: "d"}}

print(dictn["item1"][2])

print(dictn.keys())
print(dictn.values())


# _______________________time complexity ___________________________________

# time complexity to find key in dictionary is O(N)
# time complexity to get item from dictionary is O(N)
# time complexity to delete item from dictionary is O(N)
# time complexity to traverse in a dictionary is O(N)

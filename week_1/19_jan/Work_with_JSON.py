import json

# JSON: is light weight data format for data interchange

# convertion of python data into a json data

a = {1:'one',2:'two',3:'three'}

print(type(a))

a = json.dumps(a)

print(a)
print(type(a))


"""
python data          json data

dict                 object
list,tuple           array
str                  string
int,float,long       numbers
True                 true
False                false
None                 null

"""


x = {
    1:'one',
    2:2,
    3:True,
    4:[1,2,3,4],
    5:(1,2,3,4),
    6:"this is line ",
    7:{'one':1,'two':2}
}

y = json.dumps(x)
print(y)


#_____________________________format the result______________________________

z = json.dumps(x,indent=5)
print(z)

a = json.dumps(x,indent=4,separators=('.','='))
print(a)


b = json.dumps(x,indent=5,sort_keys=True)

print(b)


# ____________________convert JSON data to python object_______________________

# open json file

data = open('data1.json')

newData = json.load(data)

print(newData)
print(type(newData))

print(newData['fruit'])



#__________________________create a write json file_____________________________

dict1 = {1:'one',2:'two'}

dict1 = json.dumps(dict1)

file = open('data3.json','w')
file.write(dict1)
file.close()



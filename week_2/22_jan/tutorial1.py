
# what is __name__ ?

"""
The __name__ variable  is a special Python variable.
 It gets its value depending on how we execute the containing script.


When you run your script, the __name__ variable equals __main__.
When you import the containing script,it will contain the name of the script.

we make use of this variable to create modules in Python.



"""

# this file use as module in the tutorial2 file

def func():
    print("hello world this is tutorial1 file")

def add(a,b):
    return a+b

print("name is ",__name__)

if __name__ == '__main__':
    func()
    print(add(1, 2))

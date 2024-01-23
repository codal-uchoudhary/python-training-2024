import os

#____________________________ open() function__________________________________________

# open(): is the key function to open a file in our program

"""
'r' : read-default value
'a' : append
'w' : write
'x' : create

"""

file = open('demo.txt','r')

print(file)


#_____________________________read file _______________________________________

# we use read function to readfile

print(file.read())

print(file.read(10))  # read only 10 char from file

f = open('Demo.txt','r')
print(f.readline())              # line 1
print(f.readline())              # line 2


#______________________________close file()____________________________________

f.close()



#__________________________write a file________________________________________

f = open('Demo.txt','a')   # add content file

f.write("this is new line")
f.close()

f = open('Demo.txt','r')
print(f.read())

f.close()


f = open("Demo2.txt",'w')

f.write("this is new content added using write mode")
f.close()


f = open('Demo2.txt')
print("this is new file :   ",f.read())

f = open('Demo3.txt','w')
f.write('this file created using write mode of the file funciton')

f.close()

f = open('Demo3.txt','r')
print(f.read())


#____________________________________delete file________________________

# os.remove('useless.txt')


#_________________________check file is exist or not____________________

if os.path.exists('useless.txt'):
    print("file exist")
else:
    print("file does not exist")







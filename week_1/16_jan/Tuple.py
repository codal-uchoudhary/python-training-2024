#_________________________Tuple__________________________________________

# A tuple is a collection which is ordered and unchangeable.

tuple1 = (1,2,3,4,5)

print(type(tuple1))



list1 = [1,2,3]
tuple2 = tuple(list1)
print(type(tuple2))

#______________indexing and access item in tuple______________

tuple3 = (1,2,3,4,5,6,7,8,9,10)

print(tuple3[:])
print(tuple3[:-1])
print(tuple3[-5:-1])

print(tuple3[1:10:3])

print(tuple3[-1])

#________________________check if list is in tuple or not________________

if 100 in tuple3:
    print("100 is there in list")
else:
    print("100 is not there in list")



#________________________update or modify the tuple______________________

# we can not change the tuple , but there are some work around
# first convert tuple in to list, update the list and conver back to tuple

tuple4 = (1,2,3)
x = list(tuple4)
x[1]='changed'
tuple4 = tuple(x)
print(tuple4)


#__________________________unpack of tuple______________________________

tuple5 = (1,2,3,4,5)

(a,b,c,d,e) = tuple5
print(a," ",tuple5[0])
print(b," ",tuple5[1])

(ummed,*hari)= tuple5

print(ummed)
print(hari)
print(type(hari))

(ume,*suki,rohit)= tuple5

print(ume)
print(suki)
print(rohit)

#__________________________looping in tuple____________________________

for i in tuple5:
    print(i)

i = 0
while i < len(tuple5):
    print(tuple5[i])
    i+=1



#_________________________join tuple______________________________________

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2

print(type(t3))
print(t3)

t4 = t1*2
print(t4)


# count method

print(t4.count(1))



#_____________________________time complexity__________________________________

# Time complexity of creating a tuple is O(1)
# Time complexity fot traverse in a tuple is O(N)
# Time complexity for linear search in tuple is O(N)




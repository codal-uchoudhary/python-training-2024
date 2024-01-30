from functools import reduce

#____________________________map________________________________________

# map: this method applies a seocific function to each element of an itrable and return a new itrable

data = [1,2,3,4,5,6,7]

data1 = map(lambda x:x*10,data)

for i in data1:
    print(i)


list1 = list(map(lambda x:x*10,data))
print(list1)


# map on set

set1 = {1,2,3}

set2 = set(map(lambda x:x*x,set1))

print(set2)


# multiple itrable

l1 = [1,2,3]
l2 = [10,20,30]

ans = list(map(lambda x,y:x+y,l1,l2))
print(ans)

def square(a):
    return a*a

ans  = list(map(square,set1))

print(ans,"this is square")

#________________________________filter_______________________________

# filter: this method filter the items from a given itrable and return a new itrable

lis = [1,2,3,4,5,6,7,8,9,10]

ans_even = list(filter(lambda x: x%2 == 0 , lis))

print(ans_even)

def odd(i):
    if not i%2 == 0:
        return i;

ans_odd = list(filter(odd,lis))
print(ans_odd)




#_______________________________Reduce_______________________________

# Reduce : this method apply aggregation function on itrable data and return a single value

def add(a,b):
    return a+b

lis2 = [1,2,3,4,5]

result = reduce(add,lis2)

print(result)

# find greatest vale

def max(a,b):
    if(a>b):
        return a
    else:
        return b


result2 = reduce(max,lis2)

print(result2)


#_____________________________indexing ______________________________________

# indexing for list and tuple

lis = [1,2,3,4,5]
tup = (1,2,3,4,5)

print(lis[0],tup[0])
print(lis[:],tup[:])

print(lis[0:],tup[0:])
print(lis[:2],tup[:2])

print(lis[::2],tup[::2])
print(lis[-3:],tup[-3:])

print(lis[-3:-1],tup[-3:-1])

print(lis[2:],tup[2:])
print(lis[::-1],tup[::-1])



#____________________________zip functoin________________________________

#zip(): function returns a zip object, which is an iterator of tuples

a = (1,2,3,4,5)
b = (100,200,300,400)

c = zip(a,b)

for i in c:
    print(i)

a = [1,2,3]
b = [100,200]
x = (-1,-2)
c = zip(a,b,x,a)

for i in c:
    print(i)

print(c)
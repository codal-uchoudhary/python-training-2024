# ___________________________while loop_____________________________

i = 0

while i < 4:
    print(i, " is less than 4")
    i += 1

# break

i = 3
while True:
    if i < 0:
        break
    print(i, " is +ve")
    i = i - 1


# continue

i = -3
while i < 5:
    i += 1
    if i <= 0:
        continue
    print(i, " is greater than 0 and less than 5")


# ____________________________for loop________________________________

for i in range(4):
    print(i + 10)

for i in range(10, 15):
    print(i)


set1 = {1, 2, 3, 4, 5}

# continue statement

for i in set1:
    if i == 2:
        continue
    print(i)

# break statement

for i in set1:
    if i == 3:
        break
    print(i)

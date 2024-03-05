# working with CSV file

import csv


# read csv file

file = open("demo.csv", "r")

feilds = []
rows = []

csvreader = csv.reader(file)

header = next(csvreader)

for i in header:
    print(i, end="  ")
print("\n")


for row in csvreader:
    rows.append(row)

for i in rows:
    for j in i:
        print(j, end=" , ")
    print("\n")


# reading a csv file into a dictionary
file = open("demo.csv")
csvreader = csv.DictReader(file)

data = []

reader = csv.DictReader(file)

for row in reader:
    data.append(row)

print(data)

# ____________________________writing csv file___________________________________

head = ["id", "name", "age", "salary"]

rows = [[1, "ummed", 22, "s1"], [2, "parth", 21, "s2"]]

file = open("demo2.csv", "w")

csvwriter = csv.writer(file)

csvwriter.writerow(head)
csvwriter.writerows(rows)

# csv file created with above content


# _________________________writing dictionary to csv file__________________________

head = ["id", "roll", "company"]

rows = [
    {"id": 1, "roll": "python", "company": "codal"},
    {"id": 2, "roll": "cpp", "company": "google"},
]

file = open("demo3.csv", "w")

writer = csv.DictWriter(file, fieldnames=head)
writer.writeheader()
writer.writerows(rows)

import connect_to_database as database

conn = database.get_connection()
cursor = conn.cursor()


# _______________________________create opration_________________________________

# create table

cursor.execute("""CREATE TABLE IF NOT EXISTS person(
id INT PRIMARY KEY,
name VARCHAR(225),
country VARCHAR(225),
gender VARCHAR(225),
age INT
)""")



# insert data

cursor.execute("""INSERT INTO person(id,name,country,gender,age) VALUES
(1,'ummed','India','male',20),
(2,'leesa','usa','female',22),
(3,'manoj','India','male',30),
(4,'ranna','India','male',25),
(5,'bijesh','canada','male',33),
(6,'seema','usa','female',40),
(7,'jamna','India','female',55),
(8,'suki','India','male',30)
""")

# select all data from table

cursor.execute("SELECT * FROM person")
dataList = cursor.fetchall()

for i in dataList:   # print all the rows
    print(i)


#______________________________ read data_______________________________

# select specific column_

print("_____select specific column_______")
cursor.execute("SELECT id,name FROM person")

for i in cursor.fetchall():
    print(i)


# select distinct value

cursor.execute("SELECT DISTINCT country FROM person")
print("_____distinct country_________")
for i in cursor.fetchall():
    print(i)

# count distinct entry

cursor.execute("SELECT COUNT(DISTINCT country) FROM person")
print("_____count of distinct country______")
print(cursor.fetchone())


# count total rows

cursor.execute("SELECT count(*) FROM person")

print("____total rows are____")

print(cursor.fetchone())


# filter records
cursor.execute("SELECT * FROM person WHERE age >= 40")
print("_______filtered records (age>=40)_______")
for i in cursor.fetchall():
    print(i)

# order by keyword

cursor.execute("SELECT * FROM person ORDER BY age")

print("______ sorted data by age________")
for i in cursor.fetchall():
    print(i)


print("______ sorted data by id (decending order)______")
cursor.execute("SELECT * FROM person ORDER BY id DESC")

for i in cursor.fetchall():
    print(i)


print("______ sorted data by name(alphabetically)______")
cursor.execute("SELECT * FROM person ORDER BY name")

for i in cursor.fetchall():
    print(i)

# limit keyword

print("______ return only 5 records______")
cursor.execute("SELECT * FROM person LIMIT 5")

for i in cursor.fetchall():
    print(i)

print("______ return only 5 records starting from 4th row______")
cursor.execute("SELECT * FROM person LIMIT 5 OFFSET 3")

for i in cursor.fetchall():
    print(i)

# min and max

print("______ return the highest age______")
cursor.execute("SELECT MAX(age)  FROM person")

for i in cursor.fetchall():
    print(i)


print("______ return the lowest age______")
cursor.execute("SELECT MIN(age)  FROM person")

for i in cursor.fetchall():
    print(i)

# count



print("______ return the total rows______")
cursor.execute("SELECT COUNT(*) FROM person")

for i in cursor.fetchall():
    print(i)


print("______ return the total rows with age >=30______")
cursor.execute("SELECT COUNT(*)  FROM person where age>=30")

for i in cursor.fetchall():
    print(i)

# sum,avg


print("______ return the sum of age______")
cursor.execute("SELECT SUM(age)  FROM person")

for i in cursor.fetchall():
    print(i)


print("______ return the average of age______")
cursor.execute("SELECT AVG(age)  FROM person")

for i in cursor.fetchall():
    print(i)


# group by


print("______number of person from diffrent countries______")
cursor.execute("SELECT COUNT(age),country  FROM person GROUP BY country")

for i in cursor.fetchall():
    print(i)

print("_____ sum of age of person, countries wise")
cursor.execute("SELECT sum(age),country  FROM person GROUP BY  country")

for i in cursor.fetchall():
    print(i)


# having keyword

print("______countries with count of countries >1 ______")
cursor.execute("SELECT COUNT(*),country  FROM person GROUP BY country HAVING COUNT(*)>1")

for i in cursor.fetchall():
    print(i)




#_______________________________update data__________________________________

# update single row

cursor.execute("UPDATE person SET age=22 WHERE name = 'ummed' ")
cursor.execute("UPDATE person SET country = 'IRAN' WHERE country = 'usa'")

cursor.execute("select * from person")

for i in cursor.fetchall():
   print(i)


# update multiple coumns

cursor.execute("select * from person")

print("______before update_________")
for i in cursor.fetchall():
    print(i)

cursor.execute("UPDATE person SET age = 18,id=12 where name='suki'")

cursor.execute("select id,name,age from person where name='suki'")

print("___after update_____")
for i in cursor.fetchall():
    print(i)

# add columns
cursor.execute("SELECT * FROM person")

print("_____data before update_____")
for i in cursor.fetchall():
    print(i)

cursor.execute("ALTER TABLE person ADD state VARCHAR(225)")

cursor.execute("UPDATE person SET state='RAJ' where country='India'")

cursor.execute("SELECT * FROM person")

print("_____data after state column is added_____")
for i in cursor.fetchall():
    print(i)


# delete the column in the table

cursor.execute("SELECT * FROM person")

print("______before update _____")

for i in cursor.fetchall():
    print(i)


cursor.execute("ALTER TABLE person DROP COLUMN gender")


cursor.execute("SELECT * FROM person")

print("_______gender column is deleted _____")

for i in cursor.fetchall():
    print(i)


# rename the column in the table
cursor.execute("SELECT * FROM person")
print("______ before update _____")

for i in cursor.fetchall():
    print(i)


cursor.execute("ALTER TABLE person RENAME COLUMN age TO _age")
cursor.execute("SELECT * FROM person")

print("______column age is renamed to _age _____")

for i in cursor.fetchall():
    print(i)


#____________________________ delete opration________________________________

#  delete single row

cursor.execute("select * from person")

print("_______before delete_________")
for i in cursor.fetchall():
    print(i)

cursor.execute("DELETE FROM person WHERE name = 'jamna'")
cursor.execute("select * from person")

print("_______after delete_________")
for i in cursor.fetchall():
    print(i)


# delete multiple rows_

cursor.execute("select * from person")

print("_______ before deletde _________")
for i in cursor.fetchall():
    print(i)

cursor.execute("DELETE FROM  person WHERE country='canada'")
cursor.execute("select * from person")

print("_______after delete multiple rows_________")
for i in cursor.fetchall():
    print(i)


# delete all the rows

cursor.execute("CREATE TABLE cars(id INT,modal VARCHAR(225))")


cursor.execute("INSERT INTO cars(id,modal) VALUES(1,'m1'),(2,'m2'),(3,'m3')")
cursor.execute('SELECT * FROM cars')

print("____cars table_____")
for i in cursor.fetchall():
    print(i)

cursor.execute("DELETE FROM cars")

print("___all the rows in the cars are deleted____")
cursor.execute('SELECT * FROM cars')

for i in cursor.fetchall():
    print(i)



# truncate will empty our table

cursor.execute("INSERT INTO cars(id,modal) VALUES(3,'m1'),(4,'m2'),(5,'m3')")
cursor.execute('SELECT * FROM cars')

print("____new cars table_____")
for i in cursor.fetchall():
    print(i)

cursor.execute("truncate table cars")

print("___cars table is trucncated ____")
cursor.execute('SELECT * FROM cars')

for i in cursor.fetchall():
    print(i)




#  delete table


#  Delete the table

cursor.execute("DROP TABLE cars")

# cursor.execute('SELECT * FROM cars')  //  this will give error



conn.commit()


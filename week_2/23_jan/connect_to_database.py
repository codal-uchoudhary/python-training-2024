import psycopg2  # import module

"""
what is psycopg2 : it acts as a bridge between python and postgreSQL database. that allows 
python to intract and manipulate the data sotred in postgreSQL databases.

psycopg2 is postgreSQL adapter for python programming language.

"""


# connect database


def get_connection():
    try:
        return psycopg2.connect(
            database="postgres",
            user="postgres",
            password="ummed",
            host="localhost",
            port=5432,
        )
    except:
        return False


conn = get_connection()

# check if database is connected or not

if conn:
    print("database connected sucessfully")
else:
    print("something went wrong")


#  ____________actual work on databse________________


conn.close()  # close the database

import mysql.connector            # import module

# establish connection with mysql
conn=mysql.connector.connect(host='localhost',username='root',password='password')

# then create cursor
# my_cursor=conn.cursor()

# commands ---

# query="CREATE DATABASE new_database"        # used to create new database
# query="SHOW DATABASES"                      # used to show database
# query="CREATE TABLE students(name VARCHAR (100),age INT)"     # used to create table
# query="INSERT VALUE students(name,age) VALUES(%s,%s)"      # insert value in table
# query="SELECT * FROM students"                    # used to read data



# print database 
# for data_base in my_cursor:
#     print(data_base)

# print database in list form
# print(my_cursor.fetchall())

# insert values in table
# value=("harshad",18)
# my_cursor.execute(query,value)
# values=[("harshad",18),("kunal",12)]
# my_cursor.executemany(query,values)

# print data in tables
# for row in my_corsor :
    # print(row)
# print(my_cursor.fetchall())




# my_cursor.execute(query)

# conn.commit()
# conn.close()
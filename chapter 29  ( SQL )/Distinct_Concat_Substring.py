# mysql> CREATE TABLE students(
#     s_id INT AUTO INCREMENT PRIMARY KEY ,
#     first_name VARCHAR(50) ,
#     last_name VARCHAR (50)
# ) ;

# mysql> INSERT INTO students(first_name,last_name) VALUES
#     ("Harshad","Lnade"),("Kunal","Lande"),("Mohit","Tomar"),("Avi","Verma"),("Kunal","Lande") ;


# DISTINCT ------ show only unique values

# mysql> SELECT DISTINCT last_name FROM students ;


# CONCAT ------ join two string values

# mysql> SELECT CONCAT(first_name,last_name) AS full_name FROM students ;


# ADD ROW in TABLE

# mysql>ALTER TABLE students ADD s_email VARCHAR(100) DEFAULT "unknown" ;


# SUBSTRING ------- retrieving data from string values

# mysql> SELECT * FROM students WHERE SUBSTRING(first_name,1,1)="A" ;


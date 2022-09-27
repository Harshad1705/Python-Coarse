# mysql> CREATE TABLE students(
#     s_id INT AUTO INCREMENT PRIMARY KEY ,
#     first_name VARCHAR(50) ,
#     last_name VARCHAR (50)
# ) ;

# mysql> INSERT INTO students(first_name,last_name) VALUES
#     ("Harshad","Lande"),("Kunal","Lande"),("Mohit","Tomar"),("Avi","Verma"),("Kunal","Lande") ;


# LIKE  ---- used to select like this values 

# mysql> SELECT * FROM students WHERE first_name LIKE "%a% ;
# mysql> SELECT * FROM students WHERE first_name LIKE "_____" ;


# ORDER BY ---- used to sort values

# mysql>SELECT *FROM student ORDER BY last_name ;
# mysql>SELECT *FROM student ORDER BY last_name DECS;
# mysql>SELECT *FROM student ORDER BY last_name,first_name ;
# mysql>SELECT s_id,first_name,last_name FROM student ORDER BY 2,3 ;


# LIMIT ----- used to set limit

# mysql> SELECT * FROM students ORDER BY last_name,first_name limit 1  ;
# mysql> SELECT * FROM students WHERE first_name LIKE "%a%" ORDER BY first_name limit 1; 
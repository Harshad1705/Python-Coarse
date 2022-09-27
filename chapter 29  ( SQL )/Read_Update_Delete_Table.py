# CREATE TABLE books(
#     book_id INT PRIMARY KEY AUTO INCREAMENT ,
#     name VARCHAR (100) DEFAULT "unknown" ,
#     author_name VARCHAR(100) DEFAULT "unknown" ,
#     price INT NOT NULL 
# ) ,

# INSERT INTO books(name,author_name,price) VALUES
#     ("c++","JAWAHARLAl NEHRU",50),("JAVA","MODI JI",500), ("PYTHON","ELON MUSK,1000) ;


# FOR READ

# mysql> SELECT * FROM books ;
# mysql> SELECT name,price FROM books ;
# mysql> SELECT FROM books WHERE author="MODI JI" ;
# mysql> SELECT FROM books WHERE price<300 ;
# mysql> SELECT name AS book_name ,price FROM books ;

# FOR UPDATE 

# mysql> UPDATE books SET price=300 WHERE author="JAWAHARLAL NEHRU" ;
# mysql> UPDATE books SET price=600 WHERE book_id=2 ;

# FOR DELETE

# mysql>DELETE * FROM books ;          /// Delete all rows of bookks
# mysql> DELETE FROM books WHERE price=1000 ;

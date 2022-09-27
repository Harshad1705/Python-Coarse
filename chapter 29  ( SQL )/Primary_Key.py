# PRIMARY KEY means not to have same values of attributes 

# mysql> CREATE TABLE  insta_user(name VARCHAR (100) PRIMARY KEY,password VARCHAR (50)) ;
                            #   OR
# mysql> CREATE TABLE  insta_user(name VARCHAR (100) ,password VARCHAR (50),PRIMARY KEY(name)) ;



# Auto Increament In values Of PRIMARY KEY

# mysql> CREATE TABLE  insta_user(name VARCHAR (100) AUTO INCREAMENT ,password VARCHAR (50),PRIMARY KEY(name)) ;
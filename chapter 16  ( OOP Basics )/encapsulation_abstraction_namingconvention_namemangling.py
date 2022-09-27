# NAMING CONVENTION

# _name   convention of private name
# __name__   dunder/magic method

class Person :
    count_instance=0             
    def __init__(self,first_name,last_name,age) :
        self.first_name=first_name
        self.last_last_name=last_name
        self._age=age

p1=Person("harshad","lande",18)
print(p1._age)


# NAME MANGLING

# This only changes name of variable 

class Person2 :
    count_instance=0             
    def __init__(self,first_name,last_name,age) :
        self.first_name=first_name
        self.last_last_name=last_name
        self.__age=age

p2=Person2("harshad","lande",18)

# print(p2.age)    // error
print(p2.__dict__)
print(p2._Person2__age)
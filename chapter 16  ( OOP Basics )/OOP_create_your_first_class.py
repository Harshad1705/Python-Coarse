
class Person :
    def __init__(self,first_name,last_name,age) :
        print(" init method // constructor")
        # instance variables
        self.first_name=first_name
        self.last_last_name=last_name
        self.age=age

p1=Person("harshad","lande",18)
p2=Person("kunal","lande",12)

print(p1.first_name)
print(p2.last_last_name)
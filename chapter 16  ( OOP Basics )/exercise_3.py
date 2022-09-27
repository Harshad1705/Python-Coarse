
class Person:
    count=0
    def __init__(self,first_name,age):
        self.first_name=first_name
        self.age=age
        Person.count+=1

    

p1=Person("harshad",18)
p1=Person("harshad",18)
p1=Person("harshad",18)
p1=Person("harshad",18)
print(Person.count)
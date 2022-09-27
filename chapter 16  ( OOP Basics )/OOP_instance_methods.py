
class Person :
    def __init__(self,first_name,last_name,age) :
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def full_name(self):
        return f"{self.first_name}  {self.last_name}"

    def is_avove(self) :
        return self.age>18

p1=Person("harshad","lande",18)
p2=Person("kunal","lande",12)

print(p1.full_name())
print(p2.is_avove())

print(Person.is_avove(p2))
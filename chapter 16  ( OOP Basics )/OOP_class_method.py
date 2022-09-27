class Person :
    count_instance=0
    def __init__(self,first_name,last_name,age) :
        self.first_name=first_name
        self.last_last_name=last_name
        self.age=age
        Person.count_instance = Person.count_instance + 1

    @classmethod                      # class method
    def count__instance(cls):
        return (f"you have created {cls.count_instance} instance of {cls.__name__} class")


p1=Person("harshad","lande",18)
p2=Person("kunal","lande",12)

print(Person.count__instance())
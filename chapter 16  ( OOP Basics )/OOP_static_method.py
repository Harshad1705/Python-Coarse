class Person :
    count_instance=0             
    def __init__(self,first_name,last_name,age) :
        self.first_name=first_name
        self.last_last_name=last_name
        self.age=age
        Person.count_instance = Person.count_instance + 1

    @staticmethod
    def hello():
        print("static method called")

    @classmethod                    # class method as a constructor
    def from_string(cls,string):
        first,last,age=string.split(",")
        return cls(first,last,age)
    @classmethod                      # class method
    def count__instance(cls):
        return (f"you have created {cls.count_instance} instance of {cls.__name__} class")


p1=Person("harshad","lande",18)

Person.hello()

class Animal :
    def __init__(self,name) :
        self.name = name
    
    # abstract method  :- force to define function in subclass
    def sound(self):
        raise NotImplementedError("you have to define this finction in subclass")

class Dog(Animal):
    def __init__(self,name,breed) :
        Animal.__init__(self,name)
        self.breed=breed

    def sound(self):
        return " bhow bhow"

class Cat(Animal):
    def __init__(self,name,breed) :
        Animal.__init__(self,name)
        self.breed=breed

    


doggy=Dog("kutta ","jungli")
print(doggy.sound())

billi=Cat("billa","jungli")
print(billi.sound())
class Phone :
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=price

    def phone_name(self):
        return f"{self.brand} {self.model_name}"

    # str, repr

    def __str__(self) :
        return f"{self.brand} {self.model_name} and price is {self.price}"

    def __repr__(self) :
        return f" Phone ( \'{self.brand}\' ,  \'{self.model_name}\' , {self.price} )"

my_phone=Phone("Nokia","1100",1000)
print(my_phone)

# OPERATOR OVERLOADING

class Phone2 :
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=price

    def __add__(self,other) :                 # add their price
        return self.price+other.price

my_phone2=Phone2("Nokia","1100",1000)
my_phone3=Phone2("Nokia","1100",2000)

print(my_phone2+my_phone3)

# POLYMORPHISM

class SmartPhone :
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=price

    def phone_name(self):
        return f"{self.brand} {self.model_name}"

class FlagShip (SmartPhone):
    def __init__(self,brand,model_name,price, camera):
        SmartPhone.__init__(self,brand,model_name,price)
        self.camera=camera

    def phone_name(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"

smart=SmartPhone("redmi","note 7",12500)
flag=FlagShip("oneplus","7T",35000,"16 MP")

print(smart.phone_name())
print(flag.phone_name())
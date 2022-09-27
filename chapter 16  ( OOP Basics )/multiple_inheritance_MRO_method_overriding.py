# YES , we can derive more than one class from base class

class Phone :
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=max(price,0)
        
    def make_a_call(self,phone_number):
        print(f" CALLING {phone_number} ......")

    def full_name(self) :
        return f"{self.brand} {self.model_name}"

class SmartPhone(Phone) :
    def __init__(self,brand,model_name,price,ram,storage,camera) :
        # Phone.__init__(self,brand,model_name,price)
        #      or
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.storage=storage
        self.camera=camera

class FlagShipPhone(Phone) :
    def __init__(self,brand,model_name,price,ram,storage,camera) :
        # Phone.__init__(self,brand,model_name,price)
        #      or
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.storage=storage
        self.camera=camera

# Multiple Inheritance


class Phone2 :
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=max(price,0)
        
    def make_a_call(self,phone_number):
        print(f" CALLING {phone_number} ......")

    def full_name(self) :
        return f"{self.brand} {self.model_name}"

class SmartPhone2(Phone2) :
    def __init__(self,brand,model_name,price,ram,storage,camera) :
        # Phone.__init__(self,brand,model_name,price)
        #      or
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.storage=storage
        self.camera=camera

    def full_name(self) :
        return f"{self.brand} {self.model_name} and price {self.price}"

class FlagshipPhone2(SmartPhone2) :
    def __init__(self,brand,model_name,price,ram,storage,camera,processor) :
        super().__init__(brand,model_name,price,ram,storage,camera)
        self.processor=processor
        
    def full_name(self) :
        return f"{self.brand} {self.model_name} and price {self.price} and ram {self.ram}"


phone=Phone2("nokia","1100",1000)
smartphone=SmartPhone2("redmi","note 7",12500,"4 GB","64 GB","8 MP")
flagship=FlagshipPhone2("oneplus","7T",35000,"8 GB","128 GB","108 MP","Snapdragon 855+")

print(flagship.full_name())
# print(help(flagship))

print(isinstance(flagship,FlagshipPhone2))
print(isinstance(flagship,Phone2))
print(isinstance(smartphone,FlagshipPhone2))


print(issubclass(SmartPhone2,Phone2))
print(issubclass(SmartPhone2,FlagshipPhone2))
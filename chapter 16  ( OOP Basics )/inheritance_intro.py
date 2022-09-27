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


Phone=Phone("nokia","1100",1000)
Smartphone=SmartPhone("oneplus","5",30000,"6 GB","64 GB","48 MP")

print(Smartphone.full_name())
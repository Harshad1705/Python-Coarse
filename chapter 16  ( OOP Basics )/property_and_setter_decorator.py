class Phone :
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        
        # if price>0 :
        #     self.price=price
        # else :
        #     self.price=0
        self.price=max(price,0)
        
        # self.complete_specification=f"{self.brand} {self.model_name} and price {self.price}"

    def make_a_call(self,phone_number):
        print(f" CALLING {phone_number} ......")


    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price {self.price}"


    @property
    def price(self):
        return self.price

    @price.setter
    def price(self,new_price):
        self.price=max(new_price,0)




phone1=Phone("Redmi","Note 7",12500)
print(phone1.brand)
print(phone1.model_name)

phone1.price=500

print(phone1.price)
print(phone1.complete_specification)
    

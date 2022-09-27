class Laptop :
    def __init__(self,brand_name,model_name,price) :
        print("Laptop details")
        self.Brand_name=brand_name
        self.Model_name=model_name
        self.Price=price
        self.name=brand_name+" "+model_name
    
    def discounted_price(self,n) :
        perc=(n/100)*self.Price
        return self.Price-perc

laptop1=Laptop("ACER","Aspire 7",59000)
laptop2=Laptop("DELL","Inspiron 5",54000)

print(laptop1.Brand_name)
print(laptop2.name)

print(laptop1.discounted_price(50))
print(laptop2.discounted_price(20))
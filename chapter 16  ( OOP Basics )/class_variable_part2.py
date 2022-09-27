class Laptop :
    discount_percentage=50
    def __init__(self,brand_name,model_name,price) :
        print("Laptop details")
        self.Brand_name=brand_name
        self.Model_name=model_name
        self.Price=price
        self.name=brand_name+" "+model_name
    
    def discounted_price(self) :
        perc=(self.discount_percentage/100)*self.Price
        return self.Price-perc

# dicounct change for both laptop
# Laptop.discount_percentage=80

laptop1=Laptop("ACER","Aspire 7",59000)
laptop2=Laptop("DELL","Inspiron 5",54000)

# discount only on laptop 2

laptop2.discount_percentage=50
print(laptop2.__dict__)
print(laptop2.discounted_price())



class Laptop :
    def __init__(self,brand_name,model_name,price) :
        print("Laptop details")
        self.Brand_name=brand_name
        self.Model_name=model_name
        self.Price=price
        self.name=brand_name+" "+model_name

laptop1=Laptop("ACER","Aspire 7",59000)
laptop2=Laptop("DELL","Inspiron 5",54000)

print(laptop1.Brand_name)
print(laptop2.name)
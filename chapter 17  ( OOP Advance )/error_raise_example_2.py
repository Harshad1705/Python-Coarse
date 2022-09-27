class Mobile :
    def __init__(self,name) :
        self.name=name

class MobileStores :
    def __init__(self):
        self.mobiles=[]

    def add_mobile(self,new_mobile) :
        if isinstance(new_mobile,Mobile) :
            self.mobiles.append(new_mobile)
        else :
            raise TypeError("new mobile should be object of Mobile class")

oneplus=Mobile("oneplus 7T")
samsung="samsung galaxy s8"

mobostore=MobileStores()
mobostore.add_mobile(oneplus)
mobo=mobostore.mobiles
print(mobo[0].name)
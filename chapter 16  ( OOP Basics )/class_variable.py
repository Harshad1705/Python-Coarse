
class Circle:
    pi=3.14                             # class variable 
    def __init__(self,radius):
        self.radius=radius
    def circumfernce(self):
        return 2*Circle.pi*self.radius   # calling of class variable

c=Circle(5)
c1=Circle(8)

print(c.circumfernce())
print(Circle.circumfernce(c1))


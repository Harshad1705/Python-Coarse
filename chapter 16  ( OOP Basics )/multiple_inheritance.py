class A :
    def class_a_method (self) :
        return "i/m just a class A method"
    def hello(self):
        return " hello from class A"

class B :
    def class_b_method(self) :
        return "i/m just a class B method"
    def hello(self):
        return " hello from class B"
        
class C(A,B) :
    pass

obj=C()
print(obj.class_a_method())
print(obj.class_b_method())

print(obj.hello())
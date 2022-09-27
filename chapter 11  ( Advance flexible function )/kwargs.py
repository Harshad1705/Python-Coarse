
# kwargs (keyboard argument)
# **kwargs ( double star argument )

# kwargs as a parameter 

def fun(**kwargs) :
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items() :
        print(f" {k} : {v}")
fun(first_name="harshad",last_name="lande")
print("\n\n")


def fun(name,**kwargs) :
    print(kwargs)
    print(name)
    print(type(kwargs))
    for k,v in kwargs.items() :
        print(f" {k} : {v}")
fun( "amruta",first_name="harshad",last_name="lande")
print("\n\n")

# kwars as a argument

d={"first_name":"harshad","last_name":"lande"}
def fun(**kwargs) :
    print(kwargs)

fun(**d)
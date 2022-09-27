
# there is a problem in before's decorator function
# 1. if we give argument with function
# 2. if we have to return something

def decorator_function(any_function) :
    def wrapper_function(*args,**kwargs):
        print(" this is awesome function")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def fun(a) :
    print(f"this is function with argument {a}")
fun(5)

@decorator_function
def add(a,b):
    return a+b
print(add(6,8))
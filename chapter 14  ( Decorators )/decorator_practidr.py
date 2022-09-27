from functools import wraps
def print_function_data(any_function) :
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        print(f"you are calling {any_function.__name__} function")
        print(any_function.__doc__)
        return any_function(*args,**kwargs)
    return wrapper_function

@print_function_data
def addii(a,b):
    """ this function take two number as aggument and return their sum"""
    return a+b

print(addii(4,5))
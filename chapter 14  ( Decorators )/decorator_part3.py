def decorator_function(any_function) :
    def wrapper_function():
        """this is wrapper function """
        print(" thids is awesome function")
        any_function()
    return wrapper_function

@decorator_function
def add(a,b) :
    """this is add function"""
    return a+b
print(add.__name__)
print(add.__doc__)

# to resolve this problem

from functools import wraps
def decorator_function2(any_function) :
    @wraps(any_function)
    def wrapper_function():
        print(" thids is awesome function")
        any_function()
    return wrapper_function

@decorator_function2
def add2(a,b) :
    """this is add function"""
    return a+b
print(add2.__name__)
print(add2.__doc__)



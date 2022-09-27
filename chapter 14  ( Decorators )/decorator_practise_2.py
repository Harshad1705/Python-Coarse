
from functools import wraps
def allow_int_only(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs) :
        if all([type(i)==int for i in args]):
            return any_function(*args,**kwargs)
        print("invalid argument")
    return wrapper_function

@allow_int_only
def add_all(*args) :
    total=0
    for i in args :
        total+=i
    return total

print(add_all(1,2,3,5,4))
print(add_all(1,2,34,5,[1,2,3]))
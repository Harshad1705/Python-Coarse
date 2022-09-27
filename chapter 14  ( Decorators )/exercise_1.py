from functools import wraps
import time
def calculate_time(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        t1=time.time()
        returned_value=any_function(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f"this function took {total_time} sec")
        return returned_value
    return wrapper_function

@ calculate_time
def square(n):
    return [i**2 for i in range(1,n+1)]
    

square(1000)
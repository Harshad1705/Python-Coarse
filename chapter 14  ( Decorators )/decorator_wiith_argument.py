from functools import wraps
def only_datatype_allow(data_type) :
    def allow_int_only(any_function):
        @wraps(any_function)
        def wrapper_function(*args,**kwargs) :
            if all([type(i)==data_type for i in args]):
                return any_function(*args,**kwargs)
            print("invalid argument")
        return wrapper_function
    return allow_int_only

@ only_datatype_allow(str)
def string_join(*args) :
    string=''
    for i in args :
        string=string  +  i
    return string

print(string_join("harshad","lande"))
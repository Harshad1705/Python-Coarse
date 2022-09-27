
# Decorators - enhannces the functionality of other function

# IF WE HAVE TO ADD SOME LINE OF CODE , IN MOR THAN ONE FUNCTION WITHOUT
#  CHANGE THEIR CODE THEN WE USE DECORARTORS

def func1():
    print(" this is function 1")

def func2():
    print(" this is function 2")

# if we have to add a line ("this is awesome function") in both func1 and func2

def decorator_function(any_function) :
    def wrapper_function():
        print(" thids is awesome function")
        any_function()
    return wrapper_function

func1= decorator_function(func1)
func1()

func2 = decorator_function(func2)
func2()

#  @ use for decorator 

@ decorator_function
def func3():
    print(" this is awesome func 3")

func3()
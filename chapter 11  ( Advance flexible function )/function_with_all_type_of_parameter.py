
# parameter

#  def f(name) :

# default parameter

# def f(name="harshad") :

# * args

# def f(*args) :

# **kwargs

# def f (**kwargs) :

# order to use all these parameter 

def fun(name,*args,age="18",**kwargs) :
    print(name)
    print(args)
    print(age)
    print(kwargs)

fun("harshad",1,2,3,a=1,b=2)
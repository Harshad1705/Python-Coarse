

def multiply(num,*args) :
    multiple=1
    print(num)       # 1
    print(args)      # (2,3,4,5,6)
    for i in args :
        multiple*=i
    return multiple

print(multiply(1,2,3,4,5,6))

# if we declare parameter in function then we give minimun argument just as parameter
   # def fun(num1,num2,*args) :
   # print(fun(2,3,4,5,6))
   # print(fun())                  // error

# we use parameter before * args
   #  def fun(num1,num2,*args) :
   #  def fun(*args,num1) :              /// error
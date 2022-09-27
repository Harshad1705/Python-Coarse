
# make flexible function

# * operator
# * args

def total(a,b) :
    return a+b
print(total(4,5)) 

# print(total(1,2,3,4,5))      // error

# To deal with these problem we use * operator
# * operator create tuple of all arguments

def all_total(* args) :          # at place of args , we can write anything like num , i, etc.. but according to conventions we use args
    print(args)
    print(type(args))
all_total(1,2,3,4,5)

def sum(* args ) :
    total=0
    for i in args :
        total+=i
    return total
print(sum(1,2,3,4,5,6))

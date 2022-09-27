
def is_even5 (a) :
    if a%2==0 :
        return True
    return False





def is_even (a) :
    return  a%2==0 
    
is_even2=lambda a : a%2==0

print(is_even2(7))

# if else with lambda expression

def last_char (s) :
    if len(s)>5 :
        return True
    else :
        return False

last=lambda s : True if len(s)>5 else False

print(last("abc"))
print(last("harshad"))


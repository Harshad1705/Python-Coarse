
def divide (a,b) :
    try :
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError :
        print(" Enter both integer value")
    except :
        print("Unexpected Error")
    
print(divide(4,2))
print(divide(4,0))
print(divide(4,'2'))


print(divide(4,0))
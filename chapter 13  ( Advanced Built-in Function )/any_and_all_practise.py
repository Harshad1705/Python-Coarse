
def my_sum(*args) :
    if all([(type(i)==int or type(i)==float) for i in args]) :
        total=0
        for j in args :
            total+=j
        return total
    else :
        print("wrong input")

print(my_sum(1,2,3,4,8.6,"harshad",["hdyd","ugdy"]))

print(my_sum(1,2,3,4,8.6,))
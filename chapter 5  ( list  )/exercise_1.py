
number=list(range(1,11))

def square_list(l) :
    square=[]
    for i in number :
        square.append(i*i)
    return square

print(square_list(number))

numbers=[[3,4],1,2,[5,6]]

def total_list(numbers) :
    count=0
    for i in numbers :
        if type(i)==list :
            count+=1
    return count

print(total_list(numbers))
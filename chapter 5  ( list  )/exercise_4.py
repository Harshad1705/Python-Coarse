number=[1,2,3,4,5,6,7,8,9]

def odd_even(number) :
    odd=[]
    even=[]
    for i in number :
        if i%2==0 :
            even.append(i)
        else :
            odd.append(i)
    return [odd,even]
print(odd_even(number))
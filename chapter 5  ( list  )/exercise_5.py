
input_1=[1,2,3,8]
input_2=[1,2,3,6]

def common(input_1,input_2) :
    comman=[]
    for i in input_1 :
        for j in input_2 :
            if i==j :
                comman.append(i)
            else :
                continue
    return comman

print(common(input_1,input_2))